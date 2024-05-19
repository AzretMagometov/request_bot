from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from config import settings

router = Router()


@router.message(CommandStart())
async def start_command_handler(message: Message):
    await message.answer(text="Hello")
    for admin in settings.admins:
        await message.bot.send_message(admin, text=f"Новый пользователь\n"
                                                   f"@{message.from_user.username}\n"
                                                   f"{message.from_user.full_name}")
