from telegram import Update
from telegram.ext import (
    CommandHandler, MessageHandler, filters, ContextTypes,
    ConversationHandler
)
from db import save_user

ASK_NAME, ASK_DATE, ASK_TIME, ASK_PLACE = range(4)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Как тебя зовут?")
    return ASK_NAME

async def ask_date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['name'] = update.message.text
    await update.message.reply_text("Укажи дату рождения (в формате ГГГГ-ММ-ДД):")
    return ASK_DATE

async def ask_time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['birth_date'] = update.message.text
    await update.message.reply_text("Время рождения (по желанию, формат ЧЧ:ММ, или «нет»):")
    return ASK_TIME

async def ask_place(update: Update, context: ContextTypes.DEFAULT_TYPE):
    time = update.message.text.strip()
    context.user_data['birth_time'] = time if time.lower() != 'нет' else None
    await update.message.reply_text("Место рождения (по желанию, или «нет»):")
    return ASK_PLACE

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
