from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.personalData import PersonalData

@dp.message_handler(Command("anketa"), state=None)
async def enter_test(message: types.Message):
    await message.answer("Ismingizni kiriting")
    await PersonalData.ism.set()

@dp.message_handler(state=PersonalData.ism)
async def answer_ism(message: types.Message, state: FSMContext):
    ism = message.text
    await state.update_data(
        {"ism" : ism}
    )

    await message.answer("Familiyangizni kiriting")
    await PersonalData.next()
    # await PersonalData.email.set()

@dp.message_handler(state=PersonalData.familiya)
async def answer_familiya(message: types.Message, state: FSMContext):
    familiya = message.text
    await state.update_data(
        {"familiya" : familiya}
    )

    await message.answer("Tug'ilgan yilingizni kiriting")
    await PersonalData.next()

@dp.message_handler(state=PersonalData.tyil)
async def answer_tyil(message: types.Message, state: FSMContext):
    tyil = message.text
    await state.update_data(
        {"tyil" : tyil}
    )

    await message.answer("Manzilingizni kiriting")
    await PersonalData.next()

@dp.message_handler(state=PersonalData.manzil)
async def answer_manzil(message: types.Message, state: FSMContext):
    manzil = message.text
    await state.update_data(
        {"manzil" : manzil}
    )

    await message.answer("Emailingizni kiriting")
    await PersonalData.next()

@dp.message_handler(state=PersonalData.email)
async def answer_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(
        {"email" : email}
    )

    await message.answer("Telefon raqamingizni kiriting")
    await PersonalData.next()

@dp.message_handler(state=PersonalData.tel)
async def answer_tel(message: types.Message, state: FSMContext):
    tel = message.text
    await state.update_data(
        {"tel" : tel}
    )

    #  MA'LUMOTLARNI QAYTA O'QISH
    data = await state.get_data()
    ism = data.get("ism")
    familiya = data.get("familiya")
    tyil = data.get("tyil")
    manzil = data.get("manzil")
    email = data.get("email")
    tel = data.get("tel")

    msg = "Quyidagi ma'lumotlar qabul qilindi:\n"
    msg += f"Ismingiz {ism}\n"
    msg += f"Familiyangiz {familiya}\n"
    msg += f"Tug'ilgan yilingiz {tyil}\n"
    msg += f"Yashash joyingiz {manzil}\n"
    msg += f"Pochtangiz {email}\n"
    msg += f"Telefon raqamingiz {tel}"
    await message.answer(msg)

    await state.finish()
    # await state.reset_state(with_data=False)   #Nout xotirasida saqlash uchun