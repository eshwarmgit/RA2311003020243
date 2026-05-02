from flask import Blueprint
from controllers.vehicle_controller import schedule

vehicle_routes = Blueprint("vehicle_routes", __name__)

vehicle_routes.route("/schedule", methods=["GET"])(schedule)