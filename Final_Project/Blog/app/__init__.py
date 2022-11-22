from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
csrf.init_app(app)

from app import views, models
