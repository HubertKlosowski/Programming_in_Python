import numpy as np
from flask import Blueprint, render_template, redirect, url_for
from .trainingModel import train_model, scale_data

from .models import Iris, Species
from . import db

predict = Blueprint('predict', __name__)


@predict.route('/predict', methods=['GET'])
def home():
    iris = Iris.query.all()
    serialized_iris = [
        {
            'sepal_length': i.sepal_length,
            'sepal_width': i.sepal_width,
            'petal_length': i.petal_length,
            'petal_width': i.petal_width,
            'species_id': i.species_id
        } for i in iris
    ]
    print(serialized_iris[0])
    return render_template("predict.html")


@predict.route('/predict', methods=['POST'])
def predict_iris():
    pass
