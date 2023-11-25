from flask import Blueprint, render_template

from .models import Iris, Species
from . import db

views = Blueprint('views', __name__)


@views.route('/', methods=['GET'])
def home():
    iris = db.session.query(Iris, Species.species_name).join(Species, Iris.species_id == Species.id).all()
    return render_template("table.html", iris=iris)
