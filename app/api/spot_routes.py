from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Spot, Image

spot_routes = Blueprint('spots', __name__)

@spot_routes.route('/')
def all_spots():
  spots = Spot.query.all()
  return jsonify([spot.to_dict() for spot in spots])
