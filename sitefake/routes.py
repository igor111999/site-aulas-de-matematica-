#criar os links do nosso site
from flask import render_template, url_for, redirect
from sitefake import app, database, bcrypt
from sitefake.models import Usuario, Fotos
from flask_login import login_required, login_user, logout_user, current_user
from sitefake.forms import FormLogin, FormCriarConta, FormFoto
import os
from werkzeug.utils import secure_filename

@app.route("/",methods=["GET", "POST"])
def WEB():
    return render_template("homepage.html")

@app.route("/homepage",methods=["GET", "POST"])
def homepage():
    return render_template('homepage.html')

@app.route("/feed")
def feed():
    return render_template("feed.html")

