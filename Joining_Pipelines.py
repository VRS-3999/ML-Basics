from sklearn.pipeline import FeatureUnion

if __name__ == '__main__':
    full_pipeline = FeatureUnion(transformer_list = [
        ("num_pipeline", num_pipeline),
        ("cat_pipeline", cat_pipeline),
        ])

    housing_prepared = full_pipeline.fit_transform(housing)
    print(housing_prepared)
    print(housing_prepared.shape)
