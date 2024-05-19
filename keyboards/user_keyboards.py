from datetime import datetime

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from lexicon.lexicon import LEXICON_RU
from db.schedule import SSchedule


def create_time_kb(schedule: list[SSchedule]) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()

    for time in schedule:
        date = datetime.fromtimestamp(int(time.time) / 1000).strftime("%d/%m/%Y %H:%M:%S")
        kb_builder.row(InlineKeyboardButton(text=date, callback_data=str(time.id)))

    kb_builder.row(InlineKeyboardButton(text="Отмена", callback_data="cancel"))

    return kb_builder.as_markup()
