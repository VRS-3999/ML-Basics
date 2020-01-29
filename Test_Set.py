import numpy as np

def split_train_test(data, test_ratio):
    # np.random.seed(data)
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data)*test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

if __name__ == '__main__':
    train_set, test_set = split_train_test(housing, 0.2)
    print(len(train_set), "train + ", len(test_set), "test")
