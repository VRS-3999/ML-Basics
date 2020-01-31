#from pandas.tools.plotting import scatter_matrix
from pandas.plotting import scatter_matrix

if __name__ == '__main__':
    attributes = ["median_house_value","median_income","total_rooms","housing_median_age"]
    scatter_matrix(housing[attributes], figsize=(12,8))
