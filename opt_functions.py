import pandas as pd
import numpy as np
# MILP Optimization API
from pyscipopt import Model

#Get score from bracket
def brack_score(brack1: pd.DataFrame, data: pd.DataFrame, num_rounds: int=6) -> list:
    """
    Calculate what the score of a bracket would've been given a groundtruth bracket

    Parameters
    ----------
    brack1 : pd.DataFrame
        The bracket to be evaaluated
    data : pd.DataFrame
        The data that contains the groundtruth bracket starting in the column with index 8
    num_rounds : int, optional
        Number of rounds in the bracket, by default 6

    Returns
    -------
    list
        Score fore each round
    """
    points = [10, 20, 40, 80, 160, 320]
    score = []
    for round in range(0, num_rounds):
        score.append(320 - np.sum(np.abs(brack1.iloc[:, round].values - data.iloc[:,8 + round].values))/2*points[round])
    return score

#Return useable results from optimization output
def get_results(model: Model, x: dict[int, int]) -> pd.DataFrame:
    """
    Return useable results from optimization output

    Parameters
    ----------
    model : Model
        Model object with optimization results
    x : dict[int, int]
        Dictionary containing the optimization variables

    Returns
    -------
    pd.DataFrame
        Dataframe containing the optimization results - 1 is selected and 0 is not
    """
    out = [[model.getVal(x[i,j]) for j in range(0,6)] for i in range(0,64)]
    return pd.DataFrame(out, columns=["rd1","rd2","rd3","rd4","rd5","rd6"])

#pyscipopt code
def opt_bracket(data: pd.DataFrame, d: list[float]) -> tuple[Model, dict[int, int]]:
    """
    Function to maximize the expected points given some distance from chalk

    Parameters
    ----------
    data : pd.DataFrame
        Data that contains the probabilistic projections and the actual outcomes
    d : list[float]
        Distance from chalk per round where each value is between 0 and 1

    Returns
    -------
    tuple[Model, dict[int, int]]
        Returns the model object and the optimization variables dict
    """
    model = Model()
    probs = data.iloc[:, 2:8]
    #S = [10, 20, 40, 80, 160, 320]
    dist_norm_rounds = pd.DataFrame(data.iloc[:, 2:8].values*data.iloc[:, 14:20].values).sum()

    #Create variables
    x = {}
    for i in range(0, 64):
        for j in range(0, 6):
            x[i,j] = model.addVar(vtype="BINARY")

    #Constraint start

    #If you lose a game, cannot win the next game
    for i in range(0, 64):
        for j in range(0, 5):
            model.addCons(x[i,j+1] <= x[i, j])

    #Tournament constraints
    skip = 2
    for j in range(0,6):
        for i in range(0, 64, skip):
            model.addCons(sum([x[i,j] for i in range(i, i+skip)]) == 1)
        skip*=2

    #Distance constraints
    for j in range(0, 6):
        model.addCons(sum([x[i, j]*probs.iloc[i,j] for i in range(0,64)])/dist_norm_rounds[j] <= d[j])

    # Set objective
    # model.setObjective(sum([x[i, j] * probs.iloc[i, j] * S[j] for i in range(0, 64) for j in range(0, 6)]), "maximize")
    model.setObjective(sum([x[i, j] * probs.iloc[i, j] for i in range(0, 64) for j in range(0, 6)]), "maximize")
    
    # Set time limit
    model.setRealParam('limits/time', 60)
    
    #optimize model
    model.optimize()
    
    return model, x

#Sigmoid function for fitness function
def sigmoid(x: float, w: float=1) -> float:
    """
    Sigmoid function

    Parameters
    ----------
    x : float
        Input into the sigmoid function
    w : float, optional
        Weight that determines the steepness of the curve, by default 1

    Returns
    -------
    float
        Sigmoid output
    """
    return 1/(1+np.exp(-x/w))
