
if __name__ == '__main__':
    housing.dropna(subset=["total_bedrooms"])   #option 1
    housing.drop("total_bedrooms", axis=1)      #option 2
    median = housing["total_bedrooms"].median() #option 3
    housing["total_bedrooms"].fillna(median, inplace=True)
