from openai import OpenAI
from dotenv import load_dotenv
import os

# Cargar API Key desde archivo .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

def analizar_imagen(ruta_imagen, idioma='es', modo='chef'):
    # Simular ingredientes detectados (esto lo puedes reemplazar luego con otro sistema)
    ingredientes_detectados = ["pollo", "tomate", "queso"]

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
