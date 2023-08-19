from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData


class RoleCallback(CallbackData, prefix="role"):
    data: str


class NavigatorCallback(CallbackData, prefix="navigator"):
    data: str


class CateringCallback(CallbackData, prefix="catering"):
    data: str


class FactoryCallback(CallbackData, prefix="factory"):
    data: str


role_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Я стажёр",
                callback_data=RoleCallback(data="intern").pack()
            )
        ],
        [
            InlineKeyboardButton(
                text="Я инженер",
                callback_data=RoleCallback(data="engineer").pack()
            )
        ]
    ]
)

navigator_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Общепит",
                callback_data=NavigatorCallback(data="catering").pack()
            )
        ],
        [
            InlineKeyboardButton(
                text="Магазины",
                callback_data=NavigatorCallback(data="shops").pack()
            )
        ],
        [
            InlineKeyboardButton(
                text="Услуги",
                callback_data=NavigatorCallback(data="services").pack()
            )
        ],
        [
            InlineKeyboardButton(
                text="Афиша",
                callback_data=NavigatorCallback(data="poster").pack()
            )
        ],
        [
            InlineKeyboardButton(
                text="О заводе",
                callback_data=NavigatorCallback(data="factory").pack()
            )
        ],
    ]
)

factory_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="История",
                callback_data=FactoryCallback(data="history").pack()
            )
        ],
        [
            InlineKeyboardButton(
                text="Цифры",
                callback_data=FactoryCallback(data="numbers").pack()
            )
        ],
        [
            InlineKeyboardButton(
                text="Резиденты",
                callback_data=FactoryCallback(data="residents").pack()
            )
        ],
        [
            InlineKeyboardButton(
                text="Карта",
                callback_data=FactoryCallback(data="map").pack()
            )
        ]
    ]
)
