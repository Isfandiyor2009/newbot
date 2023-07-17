from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message

bot = Bot('6004836361:AAEqifGg36EChbUgUGKSatjlC1sFNO0E8Z4')
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: Message):
    await message.answer(f'Xush kelibsiz {message.from_user.full_name}!')

executor.start_polling(dp, skip_updates=True)