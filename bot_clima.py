import os
from dotenv import load_dotenv
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Cargar variables de entorno
load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')

# Función para obtener el clima
async def get_weather(city: str) -> str:
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': OPENWEATHER_API_KEY,
        'units': 'metric',
        'lang': 'es'
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        return f"🌤 Clima en {city}: {temp}°C, {description.capitalize()}"
    except Exception as e:
        print(f"Error al obtener clima: {e}")
        return "❌ No pude obtener el clima. Intenta más tarde."

# Comandos del bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("¡Hola! Soy un bot del clima. Usa /clima <ciudad> para saber el tiempo.")

async def clima(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await update.message.reply_text("Por favor, escribe una ciudad. Ejemplo: /clima Madrid")
        return
    
    city = ' '.join(context.args)
    weather_info = await get_weather(city)
    await update.message.reply_text(weather_info)

# Configuración principal del bot
def main() -> None:
    # Crear la aplicación y pasar el token
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Añadir manejadores de comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("clima", clima))

    # Manejo de errores
    application.add_error_handler(error_handler)

    print("Bot iniciado. Presiona Ctrl+C para detenerlo.")
    application.run_polling()

# Manejador de errores
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(f"Error: {context.error}")
    if update and hasattr(update, 'message'):
        await update.message.reply_text("❌ Ocurrió un error al procesar tu solicitud.")

if __name__ == '__main__':
    # Verificar que las variables de entorno estén configuradas
    if not TELEGRAM_TOKEN or not OPENWEATHER_API_KEY:
        print("ERROR: Faltan variables de entorno. Verifica tu archivo .env")
        exit(1)
    
    main()