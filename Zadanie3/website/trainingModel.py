from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from .models import Iris
from . import db


def count_species():
    try:
        species = db.session.query(Iris.species_id).distinct().all()
        return len(species)
    except Exception as e:
        print(e)
        return 0


def train_model(x_train, y_train, x_test, scaler):
    print("gatunki: ", count_species())
    knn = KNeighborsClassifier(n_neighbors=count_species(), weights='distance', metric='euclidean')
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
