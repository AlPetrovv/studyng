from aiogram.fsm.state import StatesGroup
from aiogram.fsm.state import State

# FSM state for registration
# StatesGroup - class that use for state object
class Reg(StatesGroup):
    # attributes of state object
    name = State()
    number = State()

