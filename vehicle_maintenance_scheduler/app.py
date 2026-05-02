import sys

# IMPORTANT: add root path (same as notification app)
sys.path.append(r"C:\Users\lenovo\Documents\GitHub\RA2311003020243")

from flask import Flask
from routes.routes import vehicle_routes

app = Flask(__name__)
app.register_blueprint(vehicle_routes)

if __name__ == "__main__":
    app.run(port=5001, debug=True)
