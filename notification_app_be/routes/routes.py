from flask import Blueprint
import controllers.notification_controller as nc

notification_routes = Blueprint("notification_routes", __name__)
notification_routes.route("/notifications", methods=["GET"])(nc.get_notifications)