from sklearn.model_selection import train_test_split

if __name__ == '__main__':

    train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)
    print(train_set,test_set)
