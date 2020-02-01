from sklearn.preprocessing import OneHotEncoder

if __name__ == '__main__':
    encoder = OneHotEncoder()
    housing_cat_1hot = encoder.fit_transform(housing_cat_encoded.reshape(-1,1))
    print(housing_cat_1hot)
    print(housing_cat_1hot.toarray())
