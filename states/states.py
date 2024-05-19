from aiogram.fsm.state import State, StatesGroup


class Request(StatesGroup):
    waiting_for_topic = State()
    waiting_for_time = State()
