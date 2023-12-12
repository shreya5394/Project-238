import os
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
load_dotenv()

# Sometimes you have folers inside folders and we want the folders to act as an application
# In these scenarios, we use __init__.py file is used to initialize the folder

# instantiate the extensions
# SQLAlchemy is used to write the SQL queries and execute SQL Queries using flask
db = SQLAlchemy()
# used to migrate the data into the database
# if there is any change in the database model, then migrate can be used to change the database models without any loss of data
migrate = Migrate()

# used to initialize the flask application
def create_app(script_info=None):
    # instantiate the app
    app = Flask(__name__)
    # cors is used to allow cross origin in an application.
    cors = CORS(app)

    # set configz
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    app.config['CORS_HEADERS'] = 'Content-Type'

    # set up extensions
    db.init_app(app)


    migrate.init_app(app, db)

    # register blueprints
    from .views.views import views
    from .api.api import api

    # blueprints can be used to set the different types of routes differently 
    # use contains the routes for the front end and api contains the routes for the back end
    app.register_blueprint(views)
    app.register_blueprint(api)

    #
    @app.errorhandler(400)
    def bad_request(e):
        return jsonify({
            "status":"error",
            "error":e.description
        }), 400

    @app.errorhandler(404)
    def not_found_error(e):
        return jsonify({
            "status":"error",
            "error":e.description
        }), 404

    @app.errorhandler(500)
    def server_error(e):
        return jsonify({
            "status":"error",
            "error":"this wasn't suppose to happen"
        })

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}
    return app
