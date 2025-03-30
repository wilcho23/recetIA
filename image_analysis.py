<<<<<<< HEAD
import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel
from openai import OpenAI
from dotenv import load_dotenv
import os

# Cargar API Key desde archivo .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

# Ingredientes conocidos
ingredientes = [
    "tomate", "cebolla", "ajo", "pollo", "papa", "zanahoria", "queso",
    "huevo", "pan", "pimiento", "lechuga", "carne", "arroz", "pepino",
    "brócoli", "coliflor", "limón", "aceite", "sal", "pasta", "berenjena"
]

# Cargar modelo CLIP
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def analizar_imagen(ruta_imagen, idioma='es', modo='chef'):
    # Detectar ingredientes con CLIP
    image = Image.open(ruta_imagen).convert("RGB")
    inputs = processor(text=ingredientes, images=image, return_tensors="pt", padding=True)
    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image
    probs = logits_per_image.softmax(dim=1)

    prob_values = probs[0].detach().numpy()
    ingredientes_detectados = [ingredientes[i] for i, p in enumerate(prob_values) if p > 0.1]

    if not ingredientes_detectados:
        return "No se detectaron ingredientes con suficiente confianza."

    # Construir prompt según idioma y modo
    ingredientes_txt = ', '.join(ingredientes_detectados)

    if idioma == 'es':
        prompt = f"Tengo los siguientes ingredientes: {ingredientes_txt}. "
        prompt += "Genera una receta completa con una lista de ingredientes y pasos de preparación detallados. "
        prompt += "Incluye tiempos de cocción y una sugerencia de acompañamiento. "
        prompt += "Separa claramente la sección de 'Ingredientes:' y 'Pasos de preparación:'. "
        prompt += "Hazlo en español. "
        if modo == 'chef':
            prompt += "Haz que la receta sea gourmet, creativa y con un toque de autor."
        else:
            prompt += "Haz que la receta sea rápida y fácil, lista en menos de 20 minutos."

    elif idioma == 'en':
        prompt = f"I have the following ingredients: {ingredientes_txt}. "
        prompt += "Generate a full recipe with a list of ingredients and detailed preparation steps. "
        prompt += "Include cooking times and a suggested side. "
        prompt += "Clearly separate 'Ingredients:' and 'Preparation Steps:'. "
        prompt += "Write it in English. "
        if modo == 'chef':
            prompt += "Make it gourmet, creative, and chef-style."
        else:
            prompt += "Make it fast and simple, ready in under 20 minutes."

    elif idioma == 'pt':
        prompt = f"Tenho os seguintes ingredientes: {ingredientes_txt}. "
        prompt += "Gere uma receita completa com lista de ingredientes e etapas de preparo detalhadas. "
        prompt += "Inclua tempos de cozimento e uma sugestão de acompanhamento. "
        prompt += "Separe claramente as seções 'Ingredientes:' e 'Modo de preparo:'. "
        prompt += "Escreva em português. "
        if modo == 'chef':
            prompt += "Faça uma receita gourmet, criativa e refinada."
        else:
            prompt += "Faça uma receita simples e rápida, pronta em menos de 20 minutos."

    # Llamada a OpenAI GPT
    try:
        respuesta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8,
            max_tokens=700
        )
        return respuesta.choices[0].message.content.strip()

    except Exception as e:
        return f"❌ Error al generar receta con GPT: {str(e)}"

=======
def analizar_imagen(ruta_imagen):
    """
    Aquí deberías incluir tu código real de análisis de imagen.
    Por ahora, esto es una simulación con ingredientes genéricos.
    """
    # TODO: reemplazar con análisis real usando visión computacional
    ingredientes_detectados = ['tomate', 'cebolla', 'ajo', 'pollo']

    receta = f"Receta sugerida con {', '.join(ingredientes_detectados)}:\n" \
             f"1. Picar los ingredientes.\n" \
             f"2. Sofreír en una sartén.\n" \
             f"3. Cocinar por 20 minutos.\n" \
             f"4. Servir caliente."

    return receta
>>>>>>> 81b10f6cdb95270b893c743a07fb7f908983890d
