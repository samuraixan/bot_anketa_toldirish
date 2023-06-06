from aiogram.dispatcher.filters.state import StatesGroup, State

class PersonalData(StatesGroup):
    ism = State()
    familiya = State()
    tyil = State()
    manzil = State()
    email = State()
    tel = State()

