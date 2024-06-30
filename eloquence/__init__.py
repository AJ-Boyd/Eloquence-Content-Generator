"""
auth: AJ Boyd
date: 6/29/2024
file: __init__.py
desc: sets up flask app for quote generators    
"""
from flask import Flask
from .routes import routes
import os

UPLOAD_FOLDER = 'uploads'
def createApp():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "i love python rahhhhhh flask is so coool way better than node js!!!ase asdfsadf sadfas"
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    
    # register blueprint
    app.register_blueprint(routes, url_prefix='/')
    return app