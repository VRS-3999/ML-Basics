from sklearn.ensemble import RandomForestRegressor

if __name__ == '__main__':
    forest_reg = RandomForestRegressor()
    forest_reg.fit(housing_prepared, housing_labels)
    housing_predictions = forest_reg.predict(housing_prepared)
    forest_mse = mean_squared_error(housing_labels, housing_predictions)
    forest_rmse = np.sqrt(forest_mse)
    print(forest_rmse)

    forest_scores = cross_val_score(forest_reg,housing_prepared, housing_labels, scoring="neg_mean_squared_error", cv=10)
    forest_rmse_scores = np.sqrt(-forest_scores)
    display_scores(forest_rmse_scores)
