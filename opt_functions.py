import pandas as pd
import numpy as np

#Get score from bracket
def brack_score(brack1, data, num_rounds=6):
    points = [10, 20, 40, 80, 160, 320]
    score = []
    for round in range(0, num_rounds):
        score.append(320 - np.sum(np.abs(brack1.iloc[:, round].values - data.iloc[:,8 + round].values))/2*points[round])
    return sum(score)

#Return useable results from optimization output
def get_results(model, x):
    out = [[model.getVal(x[i,j]) for j in range(0,6)] for i in range(0,64)]
    return pd.DataFrame(out, columns=["rd1","rd2","rd3","rd4","rd5","rd6"])

# MILP Optimization API
from pyscipopt import Model

#pyscipopt code
def opt_bracket(data, d):
    model = Model()
    probs = data.iloc[:, 2:8]
    S = [10, 20, 40, 80, 160, 320]
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
    for j in range(0,5):
        for i in range(0, 64, skip):
            model.addCons(sum([x[i,j] for i in range(i, i+skip)]) - sum([x[i,j+1] for i in range(i, i+skip)]) <= 1)
            model.addCons(sum([x[i,j] for i in range(i, i+skip)]) - sum([x[i,j+1] for i in range(i, i+skip)]) >= 0)
            model.addCons(sum([x[i,j] for i in range(i, i+skip)]) + sum([x[i,j+1] for i in range(i, i+skip)]) <= 2)
            model.addCons(sum([x[i,j] for i in range(i, i+skip)]) + sum([x[i,j+1] for i in range(i, i+skip)]) >= 1)
        skip*=2

    #Only 1 tournament winner constraint
    model.addCons(sum([x[i, 5] for i in range(0, 64)]) == 1)

    #Distance constraints
    for j in range(0, 6):
        model.addCons(sum([x[i, j]*probs.iloc[i,j] for i in range(0,64)])/dist_norm_rounds[j] <= d[j])

    # Set objective
    model.setObjective(sum([x[i, j] * probs.iloc[i, j] * S[j] for i in range(0, 64) for j in range(0, 6)]), "maximize")
    
    # Set time limit
    model.setRealParam('limits/time', 60)
    
    #optimize model
    model.optimize()
    
    return model, x

#Sigmoid function for fitness function
def sigmoid(x, w=1):
    return 1/(1+np.exp(-x/w))
