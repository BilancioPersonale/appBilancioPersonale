from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.settings.settings import SQLITE_URI


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLITE_URI
db = SQLAlchemy(app)