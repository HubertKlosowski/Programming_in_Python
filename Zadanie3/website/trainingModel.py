from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler


def train_model(x_train, y_train, x_test, scaler):
    knn = KNeighborsClassifier(n_neighbors=5)
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
    return predictions[0]


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
