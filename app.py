from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from image_analysis import analizar_imagen

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Asegurarse que la carpeta exista
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    receta = None
    if request.method == 'POST':
        if 'imagen' not in request.files:
            return 'No se envió ninguna imagen.'
        archivo = request.files['imagen']
        if archivo.filename == '':
            return 'Nombre de archivo vacío.'
        if archivo:
            nombre_seguro = secure_filename(archivo.filename)
            ruta = os.path.join(app.config['UPLOAD_FOLDER'], nombre_seguro)
            archivo.save(ruta)

            # Procesar imagen y obtener receta
            receta = analizar_imagen(ruta)

    return render_template('index.html', receta=receta)

if __name__ == '__main__':
    app.run(debug=True)
