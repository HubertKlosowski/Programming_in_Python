import numpy as np
from flask import Blueprint, render_template, redirect, url_for
from .trainingModel import train_model, scale_data

from .models import Iris, Species
from . import db

predict = Blueprint('predict', __name__)


@predict.route('/predict', methods=['GET'])
def home():
    iris = Iris.query.all()
    X = [[i.sepal_length, i.sepal_width, i.petal_length, i.petal_width] for i in iris]
    y = [i.species_id for i in iris]
    train_model(X, y, [[5.1, 3.5, 1.4, 0.2]])
    return render_template("predict.html")


@predict.route('/predict', methods=['POST'])
def predict_iris():
    pass
