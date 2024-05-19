from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def start_command_handler(message: Message, admins: list[int]):
    await message.answer(text="Hello")
    for admin_id in admins:
        await message.bot.send_message(chat_id=admin_id, text=f"Новый пользователь\n"
                                                              f"@{message.from_user.username}\n"
                                                              f"{message.from_user.full_name}")
