from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Función para conectarse a la base de datos
def get_db_connection():
    conn = sqlite3.connect('modelos.db')
    conn.row_factory = sqlite3.Row
    return conn

# Ruta principal (menú de modelos)
@app.route('/')
def index():
    print("Cargando modelos desde la base de datos...")
    conn = get_db_connection()
    modelos = conn.execute('SELECT id, nombre FROM modelos').fetchall()
    conn.close()
    return render_template('index.html', modelos=modelos)

# Ruta individual de cada modelo
@app.route('/modelo/<int:modelo_id>')
def modelo(modelo_id):
    conn = get_db_connection()
    modelo = conn.execute('SELECT * FROM modelos WHERE id = ?', (modelo_id,)).fetchone()
    conn.close()
    return render_template('modelo.html', modelo=modelo)

if __name__ == '__main__':
    app.run(debug=True)
