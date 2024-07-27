from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Load config from .env
    app.config["MONGO_URI"] = os.getenv("MONGO_URI")

    mongo.init_app(app)
    app.mongo = mongo

    # Register Blueprints
    from .views import views
    app.register_blueprint(views)

    return app
