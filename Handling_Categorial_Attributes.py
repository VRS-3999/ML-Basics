from sklearn.preprocessing import LabelEncoder

if __name__ == '__main__':
    encoder = LabelEncoder()
    housing_cat = housing["ocean_proximity"]
    housing_cat_encoded = encoder.fit_transform(housing_cat)
    print(housing_cat_encoded)
    print(encoder.classes_)
