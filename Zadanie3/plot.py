import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


df = pd.read_csv('data.csv', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species_id'])
X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y = df['species_id']
arr = ["standard", "min_max", "robust", "none"]


def train_model(x_train, y_train, x_test, scaler):
    knn = KNeighborsClassifier(n_neighbors=3, weights='distance', metric='euclidean')
    if scaler == 'standard':
        knn.fit(standard_scaler(x_train), y_train)
        predictions = knn.predict(standard_scaler(x_test))
    elif scaler == 'min_max':
        knn.fit(min_max_scaler(x_train), y_train)
        predictions = knn.predict(min_max_scaler(x_test))
    elif scaler == 'robust':
        knn.fit(robust_scaler(x_train), y_train)
        predictions = knn.predict(robust_scaler(x_test))
    else:
        knn.fit(x_train, y_train)
        predictions = knn.predict(x_test)
    return predictions


def standard_scaler(X):
    scaler = StandardScaler()
    scaler.fit(X)
    return scaler.transform(X)


def min_max_scaler(X):
    scaler = MinMaxScaler()
    scaler.fit(X)
    return scaler.transform(X)


def robust_scaler(X):
    scaler = RobustScaler()
    scaler.fit(X)
    return scaler.transform(X)


def main():
    # Jak sobie radzi z rzeczywistymi danymi
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.17, random_state=12)
    print(pd.concat([x_test, y_test], axis=1).head())
    for i in arr:
        predictions = train_model(x_train, y_train, x_test, i)
        accuracy = accuracy_score(y_test, predictions)
        print(f"Accuracy score with {i} scaler: {accuracy}")
    print()

    # Jak sobie radzi z nierzeczywistymi danymi (predykcje zmieniaja sie w zaleznosci od liczebnosci x_test
    x_test.drop(x_test.index, inplace=True)
    x_test.loc[len(x_test)] = {'sepal_length': 5.1, 'sepal_width': 3.4, 'petal_length': 1.3, 'petal_width': 0.3}  # 0
    x_test.loc[len(x_test)] = {'sepal_length': 6.3, 'sepal_width': 2.5, 'petal_length': 4.9, 'petal_width': 1.7}  # 2
    x_test.loc[len(x_test)] = {'sepal_length': 6.5, 'sepal_width': 3.0, 'petal_length': 5.2, 'petal_width': 2.0}  # 2
    for i in arr:
        predictions = train_model(X, y, x_test, i)
        print(f"Prediction with {i} scaler: {predictions}")


if __name__ == "__main__":
    main()
