#criar os links do nosso site
from flask import render_template, url_for, redirect
from sitefake import app, database, bcrypt
from sitefake.models import Usuario, Fotos
from flask_login import login_required, login_user, logout_user, current_user
from sitefake.forms import FormLogin, FormCriarConta, FormFoto
import os
from werkzeug.utils import secure_filename

@app.route("/homepage",methods=["GET", "POST"])
def homepage():
    return render_template('feed.html')



@app.route("/criarconta",methods=["GET", "POST"])
def criarconta():
    return render_template('criar_conta.html')


@app.route("/perfil", methods=["GET", "POST"])
def perfil():
    return render_template('perfil.html')


@app.route("/logout")
def logout():
    return redirect(url_for("homepage"))

@app.route("/feed")
def feed():
    return render_template("feed.html")

@app.route("/",methods=["GET", "POST"])
def WEB():
    return render_template("webproject.html")
