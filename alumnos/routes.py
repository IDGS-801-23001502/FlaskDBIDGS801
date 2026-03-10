from . import alumnos
from flask import Flask, render_template, url_for, request, redirect, flash
from models import db, Alumno
import forms

@alumnos.route("/alumnos/all")
def index():
	create_form = forms.UserForm2(request.form)
	alumno = Alumno.query.all()
	return render_template("index.html",form=create_form,alumno = alumno)

@alumnos.route("/alumnos",methods=["GET","POST"])
def Alumnos():
	create_form = forms.UserForm2(request.form)
	if request.method == "POST":
		alumno = Alumno(
			nombre = create_form.nombre.data,
			apellidos = create_form.apellidos.data,
			email = create_form.email.data,
			telefono = create_form.telefono.data
			)
		db.session.add(alumno)
		db.session.commit()
		return redirect(url_for("alumnos.index"))
	return render_template("Alumnos.html")

@alumnos.route("/alumnos/detalles")
def detalles():
	id = request.args.get('id')
	alumno = db.session.query(Alumno).filter(Alumno.id == id).first()
	return render_template("detalles.html",alumno = alumno)

@alumnos.route("/alumnos/modificar", methods=["GET","POST"])
def modificar():
	create_form = forms.UserForm2(request.form)
	if request.method == "GET" :
		id = request.args.get('id')
		alum1 = db.session.query(Alumno).filter(Alumno.id == id).first()
		create_form.id.data = alum1.id
		create_form.nombre.data = alum1.nombre
		create_form.apellidos.data = alum1.apellidos
		create_form.telefono.data = alum1.telefono
		create_form.email.data = alum1.email
	if request.method == "POST" :
		id = create_form.id.data
		alum1 = db.session.query(Alumno).filter(Alumno.id == id).first()
		alum1.nombre = str.rstrip(create_form.nombre.data)
		alum1.apellidos = create_form.apellidos.data
		alum1.email = create_form.email.data
		alum1.telefono = create_form.telefono.data
		db.session.add(alum1)
		db.session.commit()
		return redirect(url_for("alumnos.index"))
	return render_template("modificar.html", form = create_form)

@alumnos.route("/alumnos/eliminar", methods=["GET","POST"])
def eliminar():
	create_form = forms.UserForm2(request.form)
	if request.method == "GET":
		id = request.args.get("id")
		alum = db.session.query(Alumno).filter(Alumno.id == id).first()
		if alum:
			create_form.id.data = alum.id
			create_form.email.data = alum.email
			create_form.telefono.data = alum.telefono
			create_form.apellidos.data = alum.apellidos
			create_form.nombre.data = alum.nombre
			return render_template("eliminar.html", form = create_form)
	if request.method == "POST":
		id = create_form.id.data
		alum = db.session.query(Alumno).filter(Alumno.id == id).first()
		if alum :
			db.session.delete(alum)
			db.session.commit()
		return redirect(url_for("alumnos.index"))
