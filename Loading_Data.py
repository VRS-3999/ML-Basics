import os
import pandas as pd

HOUSING_PATH = os.path.join("datasets", "housing")

def load_housing_data(housing_path = HOUSING_PATH):
    csv_path = os.path.join(housing_path,"housing.csv")
    return pd.read_csv(csv_path)

if __name__ == '__main__':
    housing = load_housing_data()
    print(housing.head())    
    print(housing.info())
    print(housing["ocean_proximity"].value_counts())   
    print(housing.describe())
