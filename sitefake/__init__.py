import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://banco_mat_user:pVvo90xMSRaNk1oFInQTULmNxErNDqKE@dpg-cnervjgl6cac73cpcn70-a.oregon-postgres.render.com/banco_mat"
app.config["SECRET_KEY"] ="c3ab69c6c37bfea8b286e2942641d995"
app.config["UPLOAD_FOLDER"] = "static/fotos_post"

database = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "feed"

from sitefake import routes