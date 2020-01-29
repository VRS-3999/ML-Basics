import hashlib

def test_set_check(identifier, test_ratio, hash):
    return hash(np.int64(identifier)).digest()[-1] < 256*test_ratio

def split_train_test_by_id(data, test_ratio, id_column, hash=hashlib.md5):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio, hash))
    return data.loc[-in_test_set], data.loc[in_test_set]

if __name__ == '__main__':
    housing_with_id = housing.reset_index()
    housing_with_id["id"] = housing["longitude"]*1000+housing["latitude"]
    train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "id")
