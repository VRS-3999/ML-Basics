if __name__ == '__main__':
    housing.plot(kind="scatter", x="median_income", y="median_house_value", alpha=0.1)
    housing["rooms_per_household"] = housing["total_rooms"]/housing["households"]
    housing["bedrooms_per_room"] = housing["total_bedrooms"]/housing["total_rooms"]
    housing["population_per_household"]=housing["population"]/housing["households"]
    
    corr_matrix = housing.corr()
    print(corr_matrix["median_house_value"].sort_values(ascending = False))
