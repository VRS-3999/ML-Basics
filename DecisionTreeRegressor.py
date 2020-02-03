from sklearn.tree import DecisionTreeRegressor

if __name__ == '__main__':
    tree_reg = DecisionTreeRegressor()
    tree_reg.fit(housing_prepared, housing_labels)

    housing_prediction = tree_reg.predict(housing_prepared)
    tree_mse = mean_square_error(housing_labels, housing_predictions)
    tree_rmse = np.sqrt(tree_mse)
    print(tree_rmse)
