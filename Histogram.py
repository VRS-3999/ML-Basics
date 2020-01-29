import os
import pandas as pd
import matplotlib.pyplot as plt

HOUSING_PATH = os.path.join("datasets", "housing")

def load_housing_data(housing_path = HOUSING_PATH):
    csv_path = os.path.join(housing_path,"housing.csv")
    return pd.read_csv(csv_path)

if __name__ == 'main':
    %matplotlib inline # only in a Jupyter notebook
    housing = load_housing_data()
    housing.hist(bins=50, figsize=(20,15))
    plt.show()
