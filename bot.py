import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from handlers import user  # <-- абсолютный импорт

load_dotenv()
bot = Bot(token="5958457909:AAEcRWqp49DouHqEeWuqVaWMeM8pQXun3TQ")
dp = Dispatcher()
dp.include_router(user.router)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())
