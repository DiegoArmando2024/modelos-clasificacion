import sqlite3

# Conexión (creará la base de datos si no existe)
conn = sqlite3.connect('modelos.db')
cursor = conn.cursor()

# Crear la tabla
cursor.execute('''
CREATE TABLE IF NOT EXISTS modelos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    fuente TEXT,
    imagen TEXT
)
''')

# Confirmar cambios y cerrar
conn.commit()
conn.close()

print("Base de datos y tabla 'modelos' creadas correctamente.")
