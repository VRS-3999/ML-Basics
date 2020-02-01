from sklearn.preprocessing import impute.SimpleImputer

if __name__ == '__main__':
    imputer = impute.SimpleImputer(strategy = "median")
    housing_num = housing.drop("ocean_proximity", axis=1)
    imputer.fit(housing_num)
    print(imputer.statistics_)
    print(housing_num.median().values)
    X = imputer.transform(housing_num)
    print(X)
    housing_tr = pd.DataFrame(X, columns=housing_num.columns)
    print(housing_tr)
