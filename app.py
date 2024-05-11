from flask import Flask, send_from_directory
from flask import render_template
from flask import send_from_directory

app=Flask(__name__, template_folder='./templates')

@app.route('/')
def inicio():
    return render_template('sitio/index.html')

@app.route('/nosotros')
def nosotros():
    return render_template('sitio/nosotros.html')

@app.route('/docentes')
def docentes():
    return render_template('sitio/docentes.html')

@app.route('/galeria')
def galeria():
    return render_template('sitio/galeria.html')

@app.route('/contacto')
def contacto():
    return render_template('sitio/contacto.html')





if __name__ =='__main__':
    app.run(debug=True)
