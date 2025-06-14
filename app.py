from fastapi import FastAPI, Request
import asyncio
from bot import application
from telegram import Update
from webhook import setup_webhook

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Bot is running!"}

@app.post("/webhook")
async def telegram_webhook(req: Request):
    data = await req.json()
    update = Update.de_json(data, application.bot)
    await application.process_update(update)
    return {"ok": True}

@app.on_event("startup")
async def on_startup():
    await setup_webhook()
    await application.initialize()
