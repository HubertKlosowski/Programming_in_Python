import numpy as np
from flask import Blueprint, render_template, redirect, url_for
from .trainingModel import train_model, scale_data

from .models import Iris, Species
from . import db

predict = Blueprint('predict', __name__)


@predict.route('/predict', methods=['GET'])
def home():
    iris = Iris.query.all()
    serialized_iris = [i.to_dict(only=('sepal_length', 'sepal_width', 'petal_length', 'petal_width'))
                       for i in iris]
    return render_template("predict.html")


@predict.route('/predict', methods=['POST'])
def predict_iris():
    pass
