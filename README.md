# MarchMadnessOptimization

More details to come on the methods

### Dependencies
The dependencies required for this project are listed below. You can run `pip install -r requirements.txt` from the command line or install the dependencies to your liking using the details provided at the links below.
* [NumPy](https://numpy.org/install/)
* [Pandas](https://pandas.pydata.org/docs/getting_started/install.html)
* [Matplotlib](https://matplotlib.org/stable/users/installing/index.html)
* [Leap-ec](https://pypi.org/project/leap-ec/)
* [Dask](https://docs.dask.org/en/stable/install.html)
* [Pyscipopt](https://github.com/scipopt/PySCIPOpt)

### Data
The folder, `Data\538 Chalk Brackets\`, contains the raw forecast data obtained from FiveThirtyEight. The folder, `Data\final_bracket_data\` contains the data that was used in the calculation of this project, part of which contains the FiveThirtyEight forecast data and part of which contains other data. There are separate csv's containing data for each year with the simple naming convention `20XX.csv`. Each of the files in the that folder contain the following data:

* `Year (int)`: Year of the start of the football season
* `Week (int)`: Week within the season that the game was played
* `Name (string)`: Player Name
* `Pos (string)`: Player position
* `Team (string)`: Team for which the player played for
* `ProjDKPts (float)`: Projected Draftkings points
* `ProjFDPts (float)`: Projected FanDueal points
* `Team2 (string)`: Alternate team respresentation for "Team" field
* `Oppt (string)`: Opponent's team name
* `DK points (float)`: Actual Draftkings points
* `DK salary (float)`: Actual Draftkings salary
* `error (float)`: Difference between Draftkings projected points and actual points | `DK points - ProjDKPts`
