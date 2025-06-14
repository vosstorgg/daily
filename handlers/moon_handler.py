from telegram import Update
from telegram.ext import ContextTypes
import requests
from datetime import datetime
from config import WEATHER_API_KEY


async def moon_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    date = context.args[0] if context.args else datetime.now().strftime("%Y-%m-%d")

    try:
        url = "http://api.weatherapi.com/v1/astronomy.json"
        params = {
            "key": WEATHER_API_KEY,
            "q": "Moscow",
            "dt": date
        }
        response = requests.get(url, params=params)
        data = response.json()

        astro = data.get("astronomy", {}).get("astro", {})
        phase = astro.get("moon_phase")
        illumination = astro.get("moon_illumination")
        moonrise = astro.get("moonrise")
        moonset = astro.get("moonset")

        text = (
            f"Лунная информация на {date}:\n"
            f"Фаза Луны: *{phase}*\n"
            f"Освещённость: {illumination}%\n"
            f"Восход Луны: {moonrise or '—'}\n"
            f"Закат Луны: {moonset or '—'}"
        )

        await update.message.reply_markdown(text)

    except Exception as e:
        await update.message.reply_text(f"Не удалось получить данные 🌑\nОшибка: {e}")
