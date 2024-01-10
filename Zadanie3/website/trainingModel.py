from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


def train_model(x_train, y_train, x_test):
    knn = KNeighborsClassifier(n_neighbors=5)

    knn.fit(x_train, y_train)
    predictions = knn.predict(x_test)
    return predictions[0]
