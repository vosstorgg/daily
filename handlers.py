from telegram import Update
from telegram.ext import (
    CommandHandler, MessageHandler, filters, ContextTypes,
    ConversationHandler
)
from db import save_user
from datetime import datetime

# Состояния шагов регистрации
ASK_NAME, ASK_DATE, ASK_TIME, ASK_PLACE = range(4)

# Стартовая команда
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Как тебя зовут?")
    return ASK_NAME

# Шаг 1 — спрашиваем дату рождения
async def ask_date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['name'] = update.message.text.strip()
    await update.message.reply_text("Укажи дату рождения (в формате ДД-ММ-ГГГГ, например 25-06-1994):")
    return ASK_DATE

# Шаг 2 — парсим дату и спрашиваем время
async def ask_time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    try:
        birth_date = datetime.strptime(text, "%d-%m-%Y").date()
        context.user_data['birth_date'] = birth_date
    except ValueError:
        await update.message.reply_text("⚠️ Неверный формат даты. Введите, например: 25-06-1994")
        return ASK_DATE

    await update.message.reply_text("Время рождения (по желанию, формат ЧЧ:ММ, или «нет»):")
    return ASK_TIME

# Шаг 3 — сохраняем время и спрашиваем место
async def ask_place(update: Update, context: ContextTypes.DEFAULT_TYPE):
    time_text = update.message.text.strip()
    if time_text.lower() == 'нет':
        context.user_data['birth_time'] = None
    else:
        try:
            # Попытка преобразовать во время
            birth_time = datetime.strptime(time_text, "%H:%M").time()
            context.user_data['birth_time'] = birth_time
        except ValueError:
            await update.message.reply_text("⚠️ Неверный формат времени. Введите, например: 14:30 или «нет».")
            return ASK_TIME

    await update.message.reply_text("Место рождения (по желанию, или «нет»):")
    return ASK_PLACE

# Шаг 4 — сохраняем место и завершение
async def finish_registration(update: Update, context: ContextTypes.DEFAULT_TYPE):
    place = update.message.text.strip()
    context.user_data['birth_place'] = place if place.lower() != 'нет' else None

    # Сохраняем в БД
    await save_user(
        telegram_id=update.effective_user.id,
        name=context.user_data['name'],
        birth_date=context.user_data['birth_date'],
        birth_time=context.user_data['birth_time'],
        birth_place=context.user_data['birth_place']
    )

    await update.message.reply_text("Спасибо! Ты успешно зарегистрирован 🌟")
    return ConversationHandler.END

# Регистрируем все шаги в Telegram
def register_handlers(app):
    conv = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            ASK_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_date)],
            ASK_DATE: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_time)],
            ASK_TIME: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_place)],
            ASK_PLACE: [MessageHandler(filters.TEXT & ~filters.COMMAND, finish_registration)],
        },
        fallbacks=[],
    )
    app.add_handler(conv)

    )
    app.add_handler(conv)
