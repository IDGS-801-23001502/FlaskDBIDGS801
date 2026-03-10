from flask import Flask, render_template, url_for, request, redirect, flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask_migrate import Migrate
from models import db, Alumno
from flask import g
from maestros.routes import maestros
from alumnos.routes import alumnos
from cursos.routes import cursos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
csrf = CSRFProtect()
migrate = Migrate(app, db)
app.register_blueprint(maestros)
app.register_blueprint(alumnos)
app.register_blueprint(cursos)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404

@app.route("/")
def home():
	return render_template("home.html")
	
if __name__ == '__main__':
	csrf.init_app(app)
	with app.app_context():
		db.create_all()
	app.run()