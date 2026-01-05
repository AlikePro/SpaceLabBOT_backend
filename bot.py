import asyncio
import os
import threading

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import WebAppInfo
from fastapi import FastAPI
import uvicorn

# =====================
# Telegram Bot
# =====================

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="🚀 Open Mini App",
                    web_app=WebAppInfo(
                        url="https://alikepro.github.io/SpaceLab_BOT/"
                    )
                )
            ]
        ]
    )
    await message.answer(
        "Нажми кнопку ниже, чтобы открыть Mini App 👇",
        reply_markup=keyboard
    )

async def start_bot():
    await dp.start_polling(bot)

# =====================
# FastAPI server (for Render)
# =====================

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Bot is running"}

def start_server():
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)

# =====================
# Main
# =====================

if __name__ == "__main__":
    threading.Thread(target=start_server).start()
    asyncio.run(start_bot())
