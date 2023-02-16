# MarchMadnessOptimization

More details to come on the methods

### Description
The men's NCAA basketball tournament is a single eliminitation tournament starting with 68 teams. It is an event 

$$\max_{} F(d, X_{1}, X_{2}, ..., X_{n})$$

$$X \in \arg \max_{X \in \{0, 1\}^{T x R}} f(d, X)$$

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

### Notebooks
