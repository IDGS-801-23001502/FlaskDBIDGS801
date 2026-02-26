from wtforms import Form, StringField,IntegerField,PasswordField,FloatField,EmailField,validators
from flask_wtf import FlaskForm

class UserForm2(Form):
    id = IntegerField('id',[validators.number_range(min=1,max=20,message="Valor no valido")])
    nombre = StringField("nombre",[
        validators.DataRequired(message="El nombre es requierido"),
        validators.length(min=4,max=20,message="require min=4 max=20")
        ])
    apellidos=StringField("apellidos",[
        validators.DataRequired(message="Los apellidos son requeridos"),
        validators.length(min=3, max=10,message="Ingrese apellido valido")
    ])
    email=EmailField("correo",[
        validators.DataRequired(message="El correo es requerido"),
        validators.Email(message="Ingresa correo valido")
    ])
    telefono=StringField("telefono",[
        validators.DataRequired(message="Los telefono son requeridos"),
        validators.length(min=10, max=10,message="Ingrese telefono valido")
    ])
