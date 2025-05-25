import sqlite3
from datetime import datetime
import os

DATABASE_PATH = "modelos.db"

def get_db():
    db = sqlite3.connect(DATABASE_PATH)
    db.row_factory = sqlite3.Row
    return db

def init_db():
    db = get_db()
    with db:
        db.execute('''
            CREATE TABLE IF NOT EXISTS modelos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT NOT NULL,
                fuente TEXT NOT NULL,
                imagen TEXT NOT NULL,
                fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

# -----------------------------------------------------------
# NUEVA FUNCIÓN: Carga los modelos iniciales desde modelos.py
# -----------------------------------------------------------
from modelos import obtener_modelos

def cargar_modelos_iniciales():
    # Verificar si ya hay modelos en la base de datos
    db = get_db()
    count = db.execute('SELECT COUNT(*) FROM modelos').fetchone()[0]
    
    if count == 0:  # Solo cargar si la tabla está vacía
        modelos = obtener_modelos()
        for m in modelos:
            db.execute(
                'INSERT INTO modelos (nombre, descripcion, fuente, imagen) VALUES (?, ?, ?, ?)',
                (m.nombre, m.descripcion, m.fuente, m.imagen)
            )
        db.commit()
        print(f"✅ Se cargaron {len(modelos)} modelos iniciales en la base de datos")
    else:
        print(f"ℹ️ La base de datos ya contiene {count} modelos")