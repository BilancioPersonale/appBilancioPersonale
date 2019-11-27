from flask import Flask
from flask_sqlalchemy import SQLAlchemy

BilancioPersonale = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db =  SQLAlchemy(app)

BilancioPersonale.debug = True

if __name__ =='__main__':
    BilancioPersonale.run()