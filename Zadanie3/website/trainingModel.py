from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from .models import Iris
from . import db


def scale_data(X):
    scaler = StandardScaler()
    scaler.fit(X)
    return scaler.transform(X)


def count_species():
    try:
        species = db.session.query(Iris.species_id).distinct().all()
        return len(species)
    except Exception as e:
        print(e)
        return 0


def train_model(x_train, y_train, x_test):
    knn = KNeighborsClassifier(n_neighbors=count_species(), weights='distance', metric='euclidean')
    knn.fit(x_train, y_train)
    prediction = knn.predict(x_test)
    return prediction[0]
