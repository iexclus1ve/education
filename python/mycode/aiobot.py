import logging
from aiogram import Bot, Dispatcher, executor, types
import os
import subprocess
from sys import exit

bot_token = os.getenv("BOT_TOKEN")
if not bot_token:
    exit("Error: no token provided")

bot = Bot(token=bot_token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
usersAllowed = (12345678, )


@dp.message_handler(commands='1')
async def cmd_test1(message: types.Message):
    if message.from_user.id in usersAllowed:

        await message.answer(f"Ваш ID: {message.from_user.id}")
        await message.answer('Hello my Master')

        buttons = [
            types.InlineKeyboardButton(
                text="Stop Nextcloud", callback_data='Action 1'),
            types.InlineKeyboardButton(
                text="Start Nextcloud", callback_data='Action 2')
        ]

        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*buttons)

        await message.answer("Select an Actions", reply_markup=keyboard)

    else:
        await message.reply('This is not for you')


@dp.callback_query_handler(text="Action 1")
async def send_random_value(call: types.CallbackQuery):
    subprocess.Popen(['python3', 'service_restart.py'])
    await call.message.answer('the service NEXTCLOUD will be STOPPED immediately')
    await call.answer(text="Спасибо, что воспользовались ботом!")
    # await call.answer()


@dp.callback_query_handler(text="Action 2")
async def send_random_value(call: types.CallbackQuery):
    await call.message.answer('the service NEXTCLOUD will be STARTED immediately')
    await call.answer(text="Спасибо, что воспользовались ботом!")
    # await call.answer()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
