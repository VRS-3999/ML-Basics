if __name__ == '__main__':
    housing = strat_train_set.copy()
    housing.plot(kind="scatter", x="latitude", y="longitude")
    housing.plot(kind="scatter", x="latitude", y="longitude")
    housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4,
                 s=housing["population"]/100, label="population", figsize=(10,7),
                 c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True,)
    plt.legend()
