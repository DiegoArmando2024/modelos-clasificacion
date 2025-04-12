import sqlite3

# Conectarse a la base de datos
conn = sqlite3.connect('modelos.db')
cursor = conn.cursor()

# Eliminar todos los registros de la tabla
cursor.execute("DELETE FROM modelos")

# Guardar cambios y cerrar conexión
conn.commit()
conn.close()

print("Todos los modelos han sido eliminados de la base de datos.")
