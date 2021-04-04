import logging
from aiogram import Bot, Dispatcher, executor, types
import os
from sys import exit

bot_token = os.getenv("BOT_TOKEN")
if not bot_token:
    exit("Error: no token provided")

bot = Bot(token=bot_token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
usersAllowed = (123456789, )


@dp.message_handler(commands="Start")
async def cmd_test1(message: types.Message):
    if message.from_user.id in usersAllowed:
        await message.answer(f"Ваш ID: {message.from_user.id}")
    else:
        await message.reply('This is not for you')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
