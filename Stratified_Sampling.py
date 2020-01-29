from sklearn.model_selection import StratifiedShuffleSplit

if __name__ == '__main__':
    
    housing["income_cat"] = np.ceil(housing["median_income"]/1.5)
    housing["income_cat"].where(housing["income_cat"]<5, 5.0, inplace=True)

    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    for train_index, test_index in split.split(housing, housing["income_cat"]):
        strat_train_set = housing.loc[train_index]
        strat_test_set = housing.loc[test_index]

    print(housing["income_cat"].value_counts() / len(housing))

    for set_ in (strat_train_set, strat_test_set):
        set_.drop("income_cat", axis=1, inplace=True)
