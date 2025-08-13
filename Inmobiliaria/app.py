from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_segura'  # Cambia por un valor seguro

# Configuración base de datos SQLite
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'prospectos.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo para los prospectos/contactos
class Prospecto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(50), nullable=False)
    nombre = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    telefono = db.Column(db.String(30))
    mensaje = db.Column(db.Text)

    def __repr__(self):
        return f'<Prospecto {self.nombre} - {self.modelo}>'

# Crear las tablas al iniciar la app
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        mensaje = request.form.get('mensaje')

        nuevo_contacto = Prospecto(
            modelo='Contacto general',
            nombre=nombre,
            email=email,
            telefono='',
            mensaje=mensaje
        )
        db.session.add(nuevo_contacto)
        db.session.commit()
        flash(f"Gracias {nombre}, hemos recibido tu mensaje.", 'success')
        return redirect(url_for('contacto'))

    return render_template('contacto.html')

@app.route('/modelos', methods=['GET', 'POST'])
def modelos():
    if request.method == 'POST':
        modelo = request.form.get('modelo')
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        telefono = request.form.get('telefono')
        mensaje = request.form.get('mensaje')

        prospecto = Prospecto(
            modelo=modelo,
            nombre=nombre,
            email=email,
            telefono=telefono,
            mensaje=mensaje
        )
        db.session.add(prospecto)
        db.session.commit()

        return render_template('gracias.html', nombre=nombre, modelo=modelo)

    return render_template('modelos.html')

if __name__ == '__main__':
    # Escucha en todas las interfaces de red del PC
    app.run(host='0.0.0.0', port=5000, debug=True)









