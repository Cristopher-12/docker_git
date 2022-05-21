from flask import Flask, render_template

#Indicacion de archivo principal
app = Flask(__name__) 

#Ruta del archivo
@app.route('/') 
def principal():
    return render_template('index.html')

@app.route('/docker')
def docker():
    return render_template('docker.html')

@app.route('/ubuntu')
def ubuntu():
    return render_template('ubuntu.html')

#Arranque de archivo
if __name__ == '__main__':
    app.run(debug=True)

# Se coloca debug=true para indicar que estoy en
# modo de desarrollo y evitar reiniciar el servidor
# repetidas ocaciones.