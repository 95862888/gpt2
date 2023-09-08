import asyncio
import logging

from aiogram import Bot, Dispatcher
import config
from handlers import commands, questions


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher()

    dp.include_routers(commands.router)
    dp.include_routers(questions.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
