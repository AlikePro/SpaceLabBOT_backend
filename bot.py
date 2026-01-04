from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import WebAppInfo
import asyncio
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Хендлер для команды /start
@dp.message(Command("start"))
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[[ 
            types.InlineKeyboardButton(
                text="🚀 Open Mini App",
                web_app=WebAppInfo(
                    url="https://alikepro.github.io/SpaceLab_BOT/"
                )
            )
        ]]
    )
    await message.answer("Open the app 👇", reply_markup=kb)

async def main():
    # запускаем polling
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
