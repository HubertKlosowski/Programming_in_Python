from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


def scale_data(X):
    scaler = StandardScaler()
    scaler.fit(X)
    return scaler.transform(X)


def train_model(X_train, y_train, x_test):
    knn = KNeighborsClassifier(n_neighbors=3, weights='distance', metric='euclidean')
    knn.fit(X_train, y_train)
    prediction = knn.predict(x_test)
    return prediction[0]
