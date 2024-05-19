from aiogram import Router
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from db.users import UsersDAO
from lexicon.lexicon import LEXICON_RU
from states.states import Request

router = Router()


@router.message(CommandStart())
async def start_command_handler(message: Message, admins: list[int]):
    user = await UsersDAO.get(tg_id=message.from_user.id)
    if not user:
        await UsersDAO.add(tg_id=message.from_user.id, username=message.from_user.username)
    await message.answer(text=LEXICON_RU["start"])
    for admin_id in admins:
        await message.bot.send_message(chat_id=admin_id, text=f"Новый пользователь\n"
                                                              f"@{message.from_user.username}\n"
                                                              f"{message.from_user.full_name}")


@router.message(Command(commands=["request"]))
async def request_command_handler(message: Message, state: FSMContext):
    await message.answer(text=LEXICON_RU["request_topic"])
    await state.set_state(Request.waiting_for_topic)


@router.message(StateFilter(Request.waiting_for_topic))
async def request_topic_handler(message: Message, state: FSMContext):
    await state.update_data(topic=message.text)
    await state.set_state(Request.waiting_for_time)
    await message.answer(text=LEXICON_RU["request_time"])
