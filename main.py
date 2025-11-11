from flask import Flask, render_template, request

# Iniciamos la aplicacion con flask
app = Flask(__name__)


# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')


# Aqui hacemos la ruta para la formula 1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    # Variables para los resultados
    promedio = None
    estado = ""

    if request.method == 'POST':
        try:
            # Aqui se recogen los datos del formulario
            nota1 = int(request.form['nota1'])
            nota2 = int(request.form['nota2'])
            nota3 = int(request.form['nota3'])
            asistencia = int(request.form['asistencia'])

            # Calcula el promedio de las tres notas
            promedio = (nota1 + nota2 + nota3) / 3

            # Logica de aprobacion
            if promedio >= 40 and asistencia >= 75:
                estado = "APROBADO"
            else:
                estado = "REPROBADO"

        except ValueError:
            # Manejo de error si los campos estan vacios o no son numeros
            return render_template('ejercicio1.html', error="Por favor, ingresa todos los campos con numeros validos.")

    # Renderiza la plantilla
    return render_template('ejercicio1.html', promedio=promedio, estado=estado)


# Aqui hacemos la ruta para la formula 2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    # Variables para los resultados
    nombre_largo = ""
    longitud = 0

    if request.method == 'POST':
        # Aqui se recogen los datos del formulario
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        # Valida que los campos no esten vacios
        if not nombre1 or not nombre2 or not nombre3:
            return render_template('ejercicio2.html', error="Por favor, ingresa los tres nombres.")

        # Logica para encontrar el nombre mas largo
        nombres = [nombre1, nombre2, nombre3]

        # Usamos la funcion max() para encontrar el string mas largo
        nombre_largo = max(nombres, key=len)
        longitud = len(nombre_largo)

    # Renderiza la plantilla, pasando los resultados
    return render_template('ejercicio2.html', nombre_largo=nombre_largo, longitud=longitud)


# Aqui se ejecuta la aplicacion
if __name__ == '__main__':
    app.run(debug=True)
