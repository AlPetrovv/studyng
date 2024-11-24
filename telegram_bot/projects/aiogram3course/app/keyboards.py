from typing import AsyncGenerator

from aiogram.types import  ReplyKeyboardMarkup  # keyboard for the panel under user placeholder
from aiogram.types import  KeyboardButton  # the button that uses under the keyboard
from aiogram.types import  InlineKeyboardMarkup  # the keyboard for panel under a message
from aiogram.types import  InlineKeyboardButton # the button that uses under the message
from aiogram.utils.keyboard import InlineKeyboardBuilder  # builder for inline buttons
from aiogram.utils.keyboard import ReplyKeyboardBuilder  # builder for buttons

#####################################KEYBOARDS AND BUILDERS#########################

# create a keyboard with 3 inlines
# keyboards - init buttons + location on the panel, list by list, one list = one row
main_reply_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Каталог'), KeyboardButton(text='Помощь')],
        [KeyboardButton(text='Корзина')],
        [KeyboardButton(text='Контакты')]
    ],
    resize_keyboard=True, # change size by screen
    input_field_placeholder='Выберите пункт меню' # change placeholder text
)

# create keyboard (inline)
# Inline Button can not use only text param, must be a second param (url, callback, game, etc.)
main_inline_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="youtube", url='https://www.youtube.com/')]
    ],
)


async def get_async_cars() -> AsyncGenerator:
    for car in ('Tesla', 'Mercedes', 'BMW'): yield car

# create a keyboard by builder
async def keyboard_cars() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder() # create keyboard builder
    async for car in get_async_cars(): # async for can use if there is async function in "for"
        builder.add(KeyboardButton(text=car)) # add button to builder

    builder.adjust(2) # set 2 buttons in row
    return builder.as_markup() # builder to keyboard

# same thing as "keyboard_cars" for inline keyboard
async def inline_keyboard_cars() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    async for car in get_async_cars():
        builder.add(InlineKeyboardButton(text=car, url='https://www.youtube.com/'))

    builder.adjust(2)
    return builder.as_markup()


##########################################CALLBACK#######################
main_callback_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Каталог', callback_data='catalog'), InlineKeyboardButton(text='Помощь', callback_data='help')],
        [InlineKeyboardButton(text='Корзина', callback_data='basket')],
        [InlineKeyboardButton(text='Контакты', callback_data='contacts')]
    ],
    resize_keyboard=True, # change size by screen
    input_field_placeholder='Выберите пункт меню' # change placeholder text
)


