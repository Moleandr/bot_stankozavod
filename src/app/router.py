from aiogram import (
    Router,
    types,
    Bot,
    F
)
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from .keyboard import (
    role_keyboard,
    RoleCallback,
    navigator_keyboard,
    NavigatorCallback,
    CateringCallback,
    factory_keyboard
)
from typing import Optional
from pprint import pprint

router = Router()


async def menu(bot: Bot, call: Optional[types.CallbackQuery] = None,
               message: Optional[types.Message] = None):
    await bot.send_photo(
        chat_id=str(call.message.chat.id) if call else str(message.chat.id),
        photo='AgACAgIAAxkBAAMiZOCu_-FfHVqF3K34UdViLiEgPeUAAtHNMRtytwhL-UrK6CpUuAUBAAMCAANzAAMwBA',
        caption="Навигатор",
        reply_markup=navigator_keyboard
    )


@router.message(Command("start"))
async def start(message: types.Message, bot: Bot):
    await bot.send_video_note(
        chat_id=str(message.chat.id),
        video_note='DQACAgIAAxkBAANLZOC1WIXfVKoHQm4W2Dnpr2T0tPUAAp8zAAIWOglL6bAExPfnEvswBA'
    )
    await bot.send_message(
        chat_id=str(message.chat.id),
        text=f"Добро пожаловать на Станкозавод\nВыбери кто ты.",
        reply_markup=role_keyboard
    )


@router.message(Command("menu"))
async def menu_command(message: types.Message, bot: Bot):
    await menu(message=message, bot=bot)


@router.callback_query(RoleCallback.filter(F.data == "intern"))
async def intern(call: types.CallbackQuery, bot: Bot):
    await bot.send_message(
        chat_id=str(call.message.chat.id),
        text=f"Начнём наше путешествие.\nНа очереди первый бар: КУЙБЫШЕВ",
    )
    await bot.send_video_note(
        chat_id=str(call.message.chat.id),
        video_note='DQACAgIAAxkBAAOIZOC9rQ66ODPi3K7pWFuMkBZADD4AAvozAAIWOglLqUrCfWoWEZUwBA',
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text='Зачекиниться',
                        callback_data=CateringCallback(data="check1").pack()
                    )
                ]
            ]
        )
    )


@router.callback_query(CateringCallback.filter(F.data == "check1"))
async def check1(call: types.CallbackQuery, bot: Bot):
    await bot.send_message(
        chat_id=str(call.message.chat.id),
        text=f"Отлично отдохнули! Дальше в ПРОХОДНАЯ",
    )
    await bot.send_video_note(
        chat_id=str(call.message.chat.id),
        video_note='DQACAgIAAxkBAANpZOC6zA__8fVFVN4tkY8uQlkHubgAAtAzAAIWOglLW_3etrvHovEwBA',
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text='Зачекиниться',
                        callback_data=CateringCallback(data="check2").pack()
                    )
                ]
            ]
        )
    )


@router.callback_query(CateringCallback.filter(F.data == "check2"))
async def check2(call: types.CallbackQuery, bot: Bot):
    await bot.send_message(
        chat_id=str(call.message.chat.id),
        text=f"Вперёд в ВОЛЖАЙНУ",
    )
    await bot.send_video_note(
        chat_id=str(call.message.chat.id),
        video_note='DQACAgIAAxkBAAOjZODDya6CDY4LNlj2yF6ElZdwv2oAAjs0AAIWOglL2e43iiW3SPgwBA',
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text='Зачекиниться',
                        callback_data=CateringCallback(data="check3").pack()
                    )
                ]
            ]
        )
    )


@router.callback_query(CateringCallback.filter(F.data == "check3"))
async def check3(call: types.CallbackQuery, bot: Bot):
    await bot.send_message(
        chat_id=str(call.message.chat.id),
        text=f"Отлично провели время. Наш тур подошёл к концу.\nТеперь ты настоящий инженер!",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text='Закончить тур',
                        callback_data=CateringCallback(data="finish").pack()
                    )
                ]
            ]
        )
    )


@router.callback_query(CateringCallback.filter(F.data == "finish"))
async def finish(call: types.CallbackQuery, bot: Bot):
    await menu(call=call, bot=bot)


@router.callback_query(RoleCallback.filter(F.data == "engineer"))
async def engineer(call: types.CallbackQuery, bot: Bot):
    await menu(call=call, bot=bot)


@router.callback_query(NavigatorCallback.filter(F.data == "catering"))
async def catering(call: types.CallbackQuery, bot: Bot):
    await bot.send_photo(
        chat_id=str(call.message.chat.id),
        photo='AgACAgIAAxkBAAMpZOCwnOFtWQyR_mEmoVTH2nrHMm4AAtbNMRtytwhLFltgAcbEKZEBAAMCAAN4AAMwBA',
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text='БАР “КУЙБЫШЕВ”',
                        callback_data=CateringCallback(data="KUIBYSHEV").pack()
                    )
                ]
            ]
        )
    )
    await bot.send_photo(
        chat_id=str(call.message.chat.id),
        photo='AgACAgIAAxkBAAMvZOCxJDJLVA2w36mUAAEjeJbOehqtAALXzTEbcrcIS5m8Pd2HoD9UAQADAgADeAADMAQ',
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text='ПРОХОДНАЯ',
                        callback_data=CateringCallback(data="ENTRANCE").pack()
                    )
                ]
            ]
        )
    )
    await bot.send_photo(
        chat_id=str(call.message.chat.id),
        photo='AgACAgIAAxkBAAOrZODEFhFRwbRNONRGDfXhH-pnWxgAAkHOMRtytwhLPq3YDmi3DZMBAAMCAAN4AAMwBA',
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text='ВОЛЖАЙНА',
                        callback_data=CateringCallback(data="VOLZHAINA").pack()
                    )
                ]
            ]
        )
    )


@router.callback_query(CateringCallback.filter(F.data == "ENTRANCE"))
async def entrance(call: types.CallbackQuery, bot: Bot):
    await bot.send_video_note(
        chat_id=str(call.message.chat.id),
        video_note='DQACAgIAAxkBAANpZOC6zA__8fVFVN4tkY8uQlkHubgAAtAzAAIWOglLW_3etrvHovEwBA'
    )
    await bot.send_message(
        chat_id=str(call.message.chat.id),
        text="""Ежедневно с 16-00. Понедельник выходной.
Телефон: +79371849063""",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text='Сайт',
                        url='https://stzv.ru/residents/prohodnaya.html'
                    )
                ]
            ]
        )
    )


@router.callback_query(CateringCallback.filter(F.data == "KUIBYSHEV"))
async def kuibyshev(call: types.CallbackQuery, bot: Bot):
    await bot.send_video_note(
        chat_id=str(call.message.chat.id),
        video_note='DQACAgIAAxkBAAOIZOC9rQ66ODPi3K7pWFuMkBZADD4AAvozAAIWOglLqUrCfWoWEZUwBA'
    )
    await bot.send_message(
        chat_id=str(call.message.chat.id),
        text="""ТАНЦЕВАЛЬНЫЙ БАР С ПРЕКРАСНОЙ ВОЛЖСКОЙ КУХНЕЙ И ЖИВЫМИ КОНЦЕРТАМИ.
С 17:00 до 1:00 в будни
С 17:00 до утра в выходные
Телефон: +79677277377""",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text='Сайт',
                        url='https://stzv.ru/residents/bar-kuybyshev.html'
                    )
                ]
            ]
        )
    )


@router.callback_query(CateringCallback.filter(F.data == "VOLZHAINA"))
async def volzhaina(call: types.CallbackQuery, bot: Bot):
    await bot.send_video_note(
        chat_id=str(call.message.chat.id),
        video_note='DQACAgIAAxkBAAOjZODDya6CDY4LNlj2yF6ElZdwv2oAAjs0AAIWOglL2e43iiW3SPgwBA'
    )
    await bot.send_message(
        chat_id=str(call.message.chat.id),
        text="""БАР С ВОЛЖСКОЙ ДУШОЙ.
Работаем над графиком ;-)
Телефон:  купим)""",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text='Сайт',
                        url='https://stzv.ru/residents/volzhayna.html'
                    )
                ]
            ]
        )
    )


@router.callback_query(NavigatorCallback.filter(F.data == "factory"))
async def factory(call: types.CallbackQuery, bot: Bot):
    await bot.send_video_note(
        chat_id=str(call.message.chat.id),
        video_note='DQACAgIAAxkBAAPUZODICtQEaEGxrwIXeh2RToEo4zUAAmE0AAIWOglLH3_oZjGLdLAwBA',
        reply_markup=factory_keyboard
    )


@router.message()
async def test(message: types.Message):
    pprint(message)
