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

* `team_name (string)`: Name of the team competing
* `team_index (int)`: Arbitrary integer assigned to a team for reference
* `rdX_act (int)`: 
* `rdX_chalk (int)`: Player position
* `team_rating (float)`: Team for which the player played for
* `team_region (string)`: Projected Draftkings points
* `seed (int)`: Projected FanDueal points
