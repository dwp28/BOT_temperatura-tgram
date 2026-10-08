<h1 align="center">🌤️ ClimaBot - Asistente Meteorológico para Telegram</h1>

<p align="center">
  <em>Un bot de Telegram rápido y asíncrono para consultar el clima de cualquier ciudad en tiempo real.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/VSCode-007ACC?style=flat-square&logo=visual-studio-code&logoColor=white" alt="VSCode" />
  <img src="https://img.shields.io/badge/Telegram_API-2CA5E0?style=flat-square&logo=telegram&logoColor=white" alt="Telegram" />
  <img src="https://img.shields.io/badge/OpenWeather-E96E50?style=flat-square&logo=openweathermap&logoColor=white" alt="OpenWeather" />
</p>

<p align="center">
  <img src="telegram_image.jpg" alt="Telegram Bot Logo" width="350" />
</p>

<hr>

## 🚀 Características

- 🌍 **Consulta en tiempo real:** Obtén la temperatura y la descripción meteorológica exacta de cualquier ciudad del mundo.
- ⚡ **Interfaz sencilla e intuitiva:** Interacción directa a través de comandos básicos de Telegram.
- 🛡️ **Manejo de errores:** Respuestas amigables si la ciudad no existe, está mal escrita o si hay problemas de red.
- ⏱️ **Totalmente asíncrono:** Desarrollado utilizando `asyncio` y `python-telegram-bot` v20+ para un rendimiento óptimo.

## ⚙️ Arquitectura y Funcionamiento

El bot sigue un modelo de peticiones HTTP en bucle ("Polling"). Cuando un usuario envía un mensaje a través de Telegram, ocurre lo siguiente:

1. El bot detecta y lee el comando (ej. `/clima Madrid`).
2. Extrae el nombre de la ciudad y realiza una petición GET a la API de **OpenWeatherMap**.
3. Procesa el JSON recibido, formatea la temperatura en grados Celsius y traduce la descripción al español.
4. Devuelve el mensaje final formateado al usuario en el chat de Telegram.

## 🛠️ Tutorial de Instalación (Para Desarrolladores)

Si quieres clonar este proyecto y probarlo o modificarlo en tu propia máquina, sigue estos pasos:

### 1. Requisitos previos

- Tener **Python 3.8** o superior instalado.
- Crear un bot en Telegram a través de [@BotFather](https://t.me/botfather) y obtener tu `TOKEN`.
- Crear una cuenta en [OpenWeatherMap](https://openweathermap.org/) y obtener tu `API KEY`.

### 2. Clonar el repositorio

Abre tu terminal y ejecuta:

```bash
git clone https://github.com/dwp28/BOT_temperatura-tgram.git
cd BOT_temperatura-tgram
```

### 3. Instalar dependencias

Es altamente recomendable usar un entorno virtual. Luego, instala las librerías necesarias ejecutando:

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Crea un archivo llamado `.env` en la raíz del proyecto. **No compartas este archivo con nadie ni lo subas a GitHub**. Añade tus credenciales con esta estructura exacta:

```env
TELEGRAM_TOKEN=tu_token_de_telegram_aqui
OPENWEATHER_API_KEY=tu_api_key_de_openweather_aqui
```

### 5. Ejecutar el bot

Puedes iniciar el bot ejecutando el script de Python directamente:

```bash
python bot_clima.py
```

O utilizando el script de bash incluido (asegúrate de darle permisos de ejecución si estás en Linux/Mac con `chmod +x start.sh`):

```bash
bash start.sh
```

Verás el mensaje _"Bot iniciado. Presiona Ctrl+C para detenerlo"_ en tu consola.

## 📱 Uso del Bot

Busca tu bot en Telegram (usando el nombre de usuario que le diste en BotFather) y utiliza los siguientes comandos:

- `/start` - Inicia la conversación con el bot y recibe el mensaje de bienvenida.
- `/clima <ciudad>` - Consulta el tiempo actual en la ciudad indicada.
  - _Ejemplo 1:_ `/clima Barcelona`
  - _Ejemplo 2:_ `/clima Buenos Aires`

**Ejemplo de interacción:**

> **Usuario:** `/clima Madrid`  
> **Bot:** `🌤 Clima en Madrid: 22.5°C, Nubes dispersas`

---

## 👨‍💻 Autor

Proyecto creado y mantenido por **Daniel Willson Pastor**.

<p align="center">
  <a href="https://github.com/dwp28">
    <img src="https://img.shields.io/badge/Visit%20my%20GitHub-100000?style=flat-square&logo=github&logoColor=white" alt="GitHub" />
  </a>
  <a href="https://www.linkedin.com/in/danielwillsonpastor/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
</p>
