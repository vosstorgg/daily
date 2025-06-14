from fastapi import FastAPI, Request
import asyncio
from bot import application
from telegram import Update
from webhook import setup_webhook

app = FastAPI()

@app.post("/webhook")
async def telegram_webhook(req: Request):
    data = await req.json()
    update = Update.de_json(data, application.bot)
    await application.process_update(update)
    return {"ok": True}

@app.on_event("startup")
async def on_startup():
    import models.astro_data
    await setup_webhook()
    await application.initialize()

@app.get("/")
async def health_check():
    return {"status": "ok"}
