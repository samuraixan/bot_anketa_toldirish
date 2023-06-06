from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from states.personalData import PersonalData

from loader import dp


@dp.message_handler(CommandHelp(),state=PersonalData.ism)
async def bot_help(message: types.Message):
    text = ("Ismingizni kiriting, iltimos")

    await message.answer(text)

@dp.message_handler(CommandHelp(),state=PersonalData.familiya)
async def bot_help(message: types.Message):
    text = ("Familiyangizni kiriting, iltimos")

    await message.answer(text)

@dp.message_handler(CommandHelp(),state=PersonalData.tyil)
async def bot_help(message: types.Message):
    text = ("Tug'ilgan yilingizni kiriting, iltimos")

    await message.answer(text)

@dp.message_handler(CommandHelp(),state=PersonalData.manzil)
async def bot_help(message: types.Message):
    text = ("Manzilingizni kiriting, iltimos")

    await message.answer(text)

@dp.message_handler(CommandHelp(),state=PersonalData.email)
async def bot_help(message: types.Message):
    text = ("Emailingizni kiriting, iltimos")

    await message.answer(text)

@dp.message_handler(CommandHelp(),state=PersonalData.tel)
async def bot_help(message: types.Message):
    text = ("Telefon raqamingizni kiriting, iltimos")

    await message.answer(text)

@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")

    await message.answer("\n".join(text))
