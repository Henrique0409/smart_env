from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


cs = {
    'databasetype': 'mysql',
    'user':'root', 
    'password':'12345678',
    'at':'localhost',
    'database_name':'SMART_DATA'
    }


app = Flask(__name__)


login_manager = LoginManager(app)
app.config['SQLALCHEMY_DATABASE_URI'] = f'{cs["databasetype"]}://{cs["user"]}:{cs["password"]}@{cs["at"]}/{cs["database_name"]}'
db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=False)
from app import models
