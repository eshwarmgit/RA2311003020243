
import sys
import os
sys.path.append(r"C:\Users\lenovo\Documents\GitHub\RA2311003020224")
from flask import Flask
from routes.routes import notification_routes
import routes.routes
print(dir(routes.routes))
app = Flask(__name__)
app.register_blueprint(notification_routes)

if __name__ == "__main__":
    app.run(port=5000, debug=True)