from flask import Flask, render_template, url_for, request, redirect, flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from models import db, Alumno
from flask import g

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/alumnos",methods=["GET","POST"])
def Alumnos():
	return render_template("Alumnos.html")

if __name__ == '__main__':
	app.run(debug=True)
