from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import re
from image_analysis import analizar_imagen

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    receta = None
    ingredientes = []
    pasos = []

    if request.method == 'POST':
        # Verificar si se envió la imagen
        if 'imagen' not in request.files:
            return 'No se envió ninguna imagen.'
        archivo = request.files['imagen']
        if archivo.filename == '':
            return 'Nombre de archivo vacío.'
        if archivo:
            # Obtiene los parámetros de idioma y modo (con valores por defecto)
            idioma = request.form.get('idioma', 'es')
            modo = request.form.get('modo', 'chef')

            filename = secure_filename(archivo.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            archivo.save(path)

            # Procesar imagen y obtener la receta
            receta = analizar_imagen(path, idioma, modo)

            # Separar la receta en secciones: Ingredientes y Pasos de preparación
            ingredientes_match = re.search(r'Ingredientes:([\s\S]*?)Pasos de preparación:', receta, re.IGNORECASE)
            pasos_match = re.search(r'Pasos de preparación:([\s\S]*)', receta, re.IGNORECASE)

            if ingredientes_match:
                ingredientes = ingredientes_match.group(1).strip().split('\n')

            if pasos_match:
                raw_pasos = pasos_match.group(1).strip().split('\n')
                # Elimina números al inicio y espacios en blanco
                pasos = [re.sub(r'^\d+\.\s*', '', paso).strip() for paso in raw_pasos if paso.strip()]

    return render_template('index.html', receta=receta, ingredientes=ingredientes, pasos=pasos)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
