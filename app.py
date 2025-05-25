from flask import Flask, render_template, request, redirect, url_for, flash, abort
from werkzeug.utils import secure_filename
import os
from database import get_db, init_db, cargar_modelos_iniciales
from modelos import obtener_modelos, Modelo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta'
app.config['UPLOAD_FOLDER'] = 'static/images'

# Modelos en memoria
modelos = obtener_modelos()

@app.route('/')
def index():
    return render_template('index.html', modelos=modelos)

@app.route('/modelo/<nombre_modelo>')
def modelo_individual(nombre_modelo):
    modelo = next((m for m in modelos if m.nombre == nombre_modelo), None)
    if modelo is None:
        abort(404)
    return render_template('modelo.html', modelo=modelo, modelos=modelos)

@app.route('/almacenamiento')
def almacenamiento():
    db = get_db()
    modelos_db = db.execute('SELECT * FROM modelos').fetchall()
    # Convertir cada fila en un diccionario
    modelos_dict = [dict(m) for m in modelos_db]
    return render_template('almacenamiento.html', modelos=modelos_dict)

@app.route('/agregar_modelo', methods=['POST'])
def agregar_modelo():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        fuente = request.form['fuente']
        imagen = request.files['imagen']

        if imagen:
            filename = secure_filename(imagen.filename)
            imagen.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            db = get_db()
            db.execute(
                'INSERT INTO modelos (nombre, descripcion, fuente, imagen) VALUES (?, ?, ?, ?)',
                (nombre, descripcion, fuente, filename)
            )
            db.commit()
            flash('Modelo agregado exitosamente', 'success')

    return redirect(url_for('almacenamiento'))

@app.route('/eliminar_modelo/<int:id>', methods=['POST'])
def eliminar_modelo(id):
    db = get_db()
    db.execute('DELETE FROM modelos WHERE id = ?', (id,))
    db.commit()
    flash('Modelo eliminado exitosamente', 'success')
    return redirect(url_for('almacenamiento'))

if __name__ == '__main__':
    init_db()
    
    # 🚀 IMPORTANTE: Descomenta esta línea la primera vez para llenar la base de datos con los modelos de ML
    # cargar_modelos_iniciales()
    
    app.run(debug=True)