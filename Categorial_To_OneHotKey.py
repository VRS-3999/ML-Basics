from sklearn.preprocessing import LabelBinarizer

if __name__ == '__main__':
    encoder = LabelBinarizer()
    housing_cat_1hot = encoder.fit_transform(housing_cat)
    print(housing_cat_1hot)
