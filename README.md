# MarchMadnessOptimization

More details to come on the methods

### Description
The men's NCAA basketball tournament is a single eliminitation tournament starting with 68 teams. It's tradition to attempt to predict what the final bracket will look like before the tournament starts. Due to the sheer size of the tournament and the combinatorial nature of the bracket, it's extremely difficult to predict. In fact, there has never been a recorded perfect prediction. The best strategy to generate the most correct bracket would seem to be to select all the favorites or "chalk" in every round. Chalk could be determined by seed or another prediction method for the outcome of a game, like the projections that fivethirtyeight.com releases. Although this may seem like the best strategy, and may even provide the best performance on average, it will rarely win a bracket challenge. Although it is the most likely outcome, it's still a rare one and someone else will guess at a better bracket. Is there a way to select a bracket that is not chalk but will outperform chalk more often than not?

We can formulate this problem mathematicallly. Is there a distance from chalk that when applied to a bracket every year, the resulting bracket out performs chalk most years? This can be formulated as a bilevel optimization problem where the goal in any given year is to maximize the expected points outcome given that you are some distance from chalk and the overall goal is to maximize outperformance across all years. The year problems are the follower problem and the leader problem selects the proper distance. The problem is formulated as:

$$\max_{d \in \[0, 1\]^{R}} F(d, X_{1}^{\*}, X_{2}^{\*}, ..., X_{n}^{\*})$$

$$X_{i}^{\*} \in \underset{X_{i} \in \\{0, 1\\}^{T x R}}{\arg \max} f(d, X_{i})$$

Where $X_i$ is the braket for any given year, $d$ is the distance from chalk, $f(d, X_{i})$ is the expected score for year $i$ paramaterized by $d$, and $F(d, X_{1}^{\*}, X_{2}^{\*}, ..., X_{n}^{\*})$ is the outperformance score across all years given the distance and the optimal bracket for each year.

This notebook aims to find this distance and see if there really is a strategy better than selecting chalk every year.

### Dependencies
The dependencies required for this project are listed below. You can run `pip install -r requirements.txt` from the command line or install the dependencies to your liking using the details provided at the links below.
* [NumPy](https://numpy.org/install/)
* [Pandas](https://pandas.pydata.org/docs/getting_started/install.html)
* [Matplotlib](https://matplotlib.org/stable/users/installing/index.html)
* [Leap-ec](https://pypi.org/project/leap-ec/)
* [Dask](https://docs.dask.org/en/stable/install.html)
* [Pyscipopt](https://github.com/scipopt/PySCIPOpt) - Pyscipopt is a python API for the SCIP optimization suite, which is a non-comemrcial solver for mixed integer programming problems. The SCIP optimization suite must first be downloaded [here](https://www.scipopt.org/index.php#download). There can sometimes be issues with getting the Pyscipopt API to access the SCIP optimimiaztion suite. If you run into those issues, try consulting the feedback [here](https://github.com/scipopt/PySCIPOpt/issues/110)  

### Data
The folder, `Data\538 Chalk Brackets\`, contains the raw forecast data obtained from FiveThirtyEight. The folder, `Data\final_bracket_data\` contains the data that was used in the calculation of this project, part of which contains the FiveThirtyEight forecast data and part of which contains other data. There are separate csv's containing data for each year with the simple naming convention `20XX.csv`. Each of the files in the that folder contain the following data:

* `team_name (string)`: Name of the team competing
* `team_index (int)`: Arbitrary integer assigned to a team for reference
* `rdX_prob (float)`: Probability that the team will win that round as forecasted by FiveThirtyEight
* `rdX_act (int)`: Binary value (0 or 1) describing whether or not the team won that round when they actually played. 0 is a loss and 1 is a win 
* `rdX_chalk (int)`: Binary value (0 or 1) describing whether or not the that team was predicted to win that round given the FiveThirtyEight forecast. 0 is a projected loss and 1 is a projected win 
* `team_rating (float)`: Rating as calculated by FiveThirtyEight before the tournament started
* `team_region (string)`: Region that the team was competing in
* `seed (int)`: Seed of the team competing

### Supporting python files
* `opt_functions.py`: This file contains the functions required to carry out the optimization. The helper functions include the lower-level optimization function, a function to transform the pyscipopt output to a useable dataframe, a function to calculate the score of a bracket, and a sigmoid function.

### Notebooks
* `outperform_chalk.ipynb`: This notebook carries out the bilevel programming problem and displays the results.
* `fitness_experiments.ipynb`: This notebook explores the erosion of synchronous fitness evaluation for variable time fitness functions 
