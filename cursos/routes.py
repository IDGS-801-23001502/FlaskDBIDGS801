from . import cursos
from flask import render_template, request, redirect, url_for
from models import db,Curso,Alumno,Maestros
import forms

@cursos.route("/cursos/")
def allCursos():
    cursos = Curso.query.all();
    return render_template('/cursos/list.html',cursos = cursos)

@cursos.route("/cursos/new",methods=["GET","POST"])
def createCurso():
    create_form = forms.CursoForm(request.form)
    if request.method == "POST":
        curso = Curso(
            nombre =  create_form.nombre.data,
            descripcion =  create_form.descripcion.data,
            maestro_id =  create_form.maestro_id.data
        )
        db.session.add(curso)
        db.session.commit()
        return redirect(url_for("cursos.allCursos"))
    maestros = Maestros.query.all()
    return render_template("/cursos/new.html", maestros = maestros)

@cursos.route("/cursos/inscripcion/", methods=["GET", "POST"])
def inscripcionCurso():
    id_curso = request.args.get("id")
    curso = Curso.query.get_or_404(id_curso)
    if request.method == "POST":
        ids_seleccionados = request.form.getlist("alumnos_ids")
        for alumno_id in ids_seleccionados:
            alumno = Alumno.query.get(alumno_id)
            if alumno and alumno not in curso.alumnos:
                curso.alumnos.append(alumno)
        db.session.commit()
        return redirect(url_for('cursos.inscripcionCurso', id=id_curso))
    inscritos_ids = [a.id for a in curso.alumnos]
    alumnos_disponibles = Alumno.query.filter(~Alumno.id.in_(inscritos_ids)).all()
    
    return render_template("/cursos/inscripcion.html", 
                           curso=curso, 
                           alumnos=alumnos_disponibles)

@cursos.route("/cursos/detalles/")
def detalleCurso():
    id = request.args.get("id")
    curso = Curso.query.get_or_404(id)
    return render_template('/cursos/detalle.html', curso=curso)