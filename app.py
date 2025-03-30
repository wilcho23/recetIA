<<<<<<< HEAD
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import re
=======
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
>>>>>>> 81b10f6cdb95270b893c743a07fb7f908983890d
from image_analysis import analizar_imagen

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
<<<<<<< HEAD
=======

# Asegurarse que la carpeta exista
>>>>>>> 81b10f6cdb95270b893c743a07fb7f908983890d
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    receta = None
<<<<<<< HEAD
    ingredientes = []
    pasos = []

    if request.method == 'POST':
        archivo = request.files['imagen']
        idioma = request.form.get('idioma', 'es')
        modo = request.form.get('modo', 'chef')

        if archivo and archivo.filename != '':
            filename = secure_filename(archivo.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            archivo.save(path)

            # Análisis con IA
            receta = analizar_imagen(path, idioma, modo)

            # Separar receta en ingredientes y pasos
            ingredientes_match = re.search(r'Ingredientes:([\s\S]*?)Pasos de preparación:', receta, re.IGNORECASE)
            pasos_match = re.search(r'Pasos de preparación:([\s\S]*)', receta, re.IGNORECASE)

            ingredientes = ingredientes_match.group(1).strip().split('\n') if ingredientes_match else []

            if pasos_match:
                raw_pasos = pasos_match.group(1).strip().split('\n')
                pasos = [re.sub(r'^\d+\.\s*', '', paso).strip() for paso in raw_pasos if paso.strip()]

    return render_template('index.html', receta=receta, ingredientes=ingredientes, pasos=pasos)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)



=======
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
>>>>>>> 81b10f6cdb95270b893c743a07fb7f908983890d
