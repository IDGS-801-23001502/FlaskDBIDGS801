from . import maestros
from flask import render_template, request, redirect, url_for
import forms
from models import Maestros, db

@maestros.route("/maestros/")
def allMaestros():
    maestro = Maestros.query.all()
    return render_template("maestros/listadoMaestros.html",maestro = maestro)

@maestros.route("/maestros/new",methods=["GET","POST"])
def newMaestros():
	create_form = forms.UserForm(request.form)
	if request.method == "POST":
		maestros = Maestros(
			nombre = create_form.nombre.data,
			apellidos = create_form.apellidos.data,
			email = create_form.email.data,
			especialidad = create_form.especialidad.data
			)
		db.session.add(maestros)
		db.session.commit()
		return redirect(url_for("maestros.allMaestros"))
	return render_template("/maestros/maestros.html")

@maestros.route("/maestros/detalles")
def detalles():
	matricula = request.args.get('matricula')
	maestro = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
	return render_template("/maestros/detalles.html",maestro = maestro)

@maestros.route("/maestros/modificar", methods=["GET","POST"])
def modificar():
	create_form = forms.UserForm(request.form)
	if request.method == "GET" :
		matricula = request.args.get('matricula')
		maestro1 = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
		create_form.matricula.data = maestro1.matricula
		create_form.nombre.data = maestro1.nombre
		create_form.apellidos.data = maestro1.apellidos
		create_form.email.data = maestro1.email
		create_form.especialidad.data = maestro1.especialidad
	if request.method == "POST" :
		matricula = create_form.matricula.data
		maestro1 = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
		maestro1.nombre = str.rstrip(create_form.nombre.data)
		maestro1.apellidos = create_form.apellidos.data
		maestro1.email = create_form.email.data
		maestro1.especialidad = create_form.especialidad.data
		db.session.add(maestro1)
		db.session.commit()
		return redirect(url_for("maestros.allMaestros"))
	return render_template("/maestros/modificar.html", form = create_form)

@maestros.route("/maestros/eliminar", methods=["GET","POST"])
def eliminar():
	create_form = forms.UserForm(request.form)
	if request.method == "GET":
		matricula = request.args.get("matricula")
		maes = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
		if maes:
			create_form.matricula.data = maes.matricula
			create_form.email.data = maes.email
			create_form.apellidos.data = maes.apellidos
			create_form.nombre.data = maes.nombre
			create_form.especialidad.data = maes.especialidad
			return render_template("/maestros/eliminar.html", form = create_form)
	if request.method == "POST":
		matricula = create_form.matricula.data
		maes = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
		if maes :
			db.session.delete(maes)
			db.session.commit()
		return redirect(url_for("maestros.allMaestros"))

@maestros.route("/perfil/<nombre>")
def perfil(nombre):
    return f"Perfil {nombre}"