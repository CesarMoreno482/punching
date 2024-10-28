from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Cambia esto por una clave secreta real

# Simulando una base de datos
registros = []
nombres_validos = {}  # Cambiamos a un diccionario vacío para almacenar dinámicamente

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form['nombre']
        if nombre in nombres_validos:  # Comprobar si el nombre es válido
            hora_entrada = datetime.now().strftime("%H:%M:%S")  # Obtener la hora actual
            id_registro = nombres_validos[nombre]
            registros.append({'id': id_registro, 'nombre': nombre, 'entrada': hora_entrada, 'salida': None})
            return redirect(url_for('index'))
        else:
            flash('Nombre inválido, por favor intenta de nuevo.')

    return render_template('index.html', registros=registros)

@app.route('/salida/<int:id>')
def salida(id):
    for registro in registros:
        if registro['id'] == id and registro['salida'] is None:
            registro['salida'] = datetime.now().strftime("%H:%M:%S")  # Registrar la hora de salida
            break
    return redirect(url_for('index'))

@app.route('/agregar_nombre', methods=['GET', 'POST'])
def agregar_nombre():
    if request.method == 'POST':
        nombre = request.form['nombre']
        id_nombre = request.form['id']
        if nombre and id_nombre:
            nombres_validos[nombre] = int(id_nombre)  # Agregar nombre y ID a los nombres válidos
            flash('Nombre agregado exitosamente.')
            return redirect(url_for('agregar_nombre'))

    return render_template('agregar_nombre.html')

if __name__ == '__main__':
    app.run(debug=True)