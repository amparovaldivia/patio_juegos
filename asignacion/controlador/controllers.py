from asignacion import app
from flask import  render_template

@app.route('/play1')
def ruta():
    return render_template('play1.html')


@app.route('/play2/<int:numero>')
def repetir_cuadrados(numero):
    return render_template('play2.html',numero=numero)

@app.route('/play2/<int:numero>/<color>')
def repetir_cuadrados_color(numero,color):
    return render_template('play2.html',numero=numero,color=color)    
