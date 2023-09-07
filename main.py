from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ParseMode, WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from aiogram.utils.markdown import *
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import datetime
from aiogram.dispatcher import filters

bot = Bot(token="5644768745:AAGOrfSr-ZI62Dylu6PXVgp4IBXBDFEf70U")
dp = Dispatcher(bot)

web_app = WebAppInfo(url="https://maximilian13.github.io/Maximilian13071999.github.io/")
kb_main = ReplyKeyboardMarkup(resize_keyboard=True)
kb_main.add(KeyboardButton(text="Game", web_app=web_app))

attemps = 3

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if attemps > 0:
        await message.answer(f"Начать игру!\n\n"
                         f"У вас только {attemps} попыток выиграть!", reply_markup=kb_main)
    else:
        await message.answer(f"У вас кончились попытки!", reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(content_types="web_app_data")
async def get_data(web_app_message):
    global attemps
    if (web_app_message.web_app_data.data == "win"):
        attemps += 1
        await web_app_message.answer(f"Хотите сыграть ещё раз?!\n\n"
                         f"У вас теперь {attemps} попыток!",
                                     reply_markup=kb_main)
    else:
        attemps -= 1
        if attemps > 0:
            await web_app_message.answer(f"Начать игру!\n\n"
                                         f"У вас только {attemps} попыток выиграть!",
                                         reply_markup=kb_main)
        else:
            await web_app_message.answer(f"У вас кончились попытки!", reply_markup=types.ReplyKeyboardRemove())

executor.start_polling(dp, skip_updates=True)