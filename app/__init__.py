from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import config

app = Flask(__name__)
app.config.from_object(os.environ.get('FLASK_ENV') or 'config.DevelopmentConfig')

db = SQLAlchemy(app)

from . import views