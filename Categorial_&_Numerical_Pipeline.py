if __name__ == '__main__':
    num_attribs = list(housing_num)
    cat_attribs = ["ocean_proximity"]

    class NewLabelBinarizer(LabelBinarizer):
        def fit(self, X, y=None):
            return super(NewLabelBinarizer, self).fit(X)
        def transform(self, X, y=None):
            return super(NewLabelBinarizer, self).transform(X)
        def fit_transform(self, X, y=None):
            return super(NewLabelBinarizer, self).fit(X).transform(X)
    
    num_pipeline = Pipeline([
        ('selector', DataFrameSelector(num_attribs)),
        ('imputer', Imputer(strategy = "median")),
        ('attribs_adder', CombinedAttributesAdder()),
        ('std_scaler', StandardScaler()),
        ])
    cat_pipeline = Pipeline([
        ('selector', DataFrameSelector(cat_attribs)),
        ('label_binarizer', NewLabelBinarizer()),
        ])
