from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def scale_data(X):
    scaler = StandardScaler()
    scaler.fit(X)
    return scaler.transform(X)


def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=1.0, shuffle=True)
    print(len(X_train))
    print(len(X_test))
    print(len(y_train))
    print(len(y_test))
    """
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)
    return knn
    """
