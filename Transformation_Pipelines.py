from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

if __name__ == '__main__':
    num_pipeline = Pipeline([
        ('imputer',Imputer(strategy="median")),
        ('attribs_adder', CombinedAttributesAdder()),
        ('std_scaler',StandardScaler()),
        ])
    housing_num_tr = num_pipeline.fit_transform(housing_num)
    print(housing_num_tr)
        
