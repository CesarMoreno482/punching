import sqlite3

# Crear la base de datos y la tabla
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS registros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    entrada TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    salida TIMESTAMP
)
''')

conn.commit()
conn.close()
