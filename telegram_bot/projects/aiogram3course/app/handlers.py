
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router
from app.states import Reg
from app.keyboards import main_reply_menu, main_inline_menu, keyboard_cars, main_callback_menu, inline_keyboard_cars
from aiogram.fsm.context import FSMContext  # Control of state
from app.middleware import TestMiddleware
router = Router()

##################################MIDDLEWARE####################################
# ## INNER MIDDLEWARE
# working everytime when use message
router.message.middleware(TestMiddleware())
# ## etc...
router.callback_query.middleware(TestMiddleware())
router.business_connection.middleware(TestMiddleware())
router.business_message.middleware(TestMiddleware())
router.channel_post.middleware(TestMiddleware())
router.chat_boost.middleware(TestMiddleware())
router.chat_join_request.middleware(TestMiddleware())
router.chat_member.middleware(TestMiddleware())
router.chosen_inline_result.middleware(TestMiddleware())
router.deleted_business_messages.middleware(TestMiddleware)
router.edited_business_message.middleware(TestMiddleware())
router.error.middleware(TestMiddleware())

# ## OUTER MIDDLEWARE
router.message.outer_middleware(TestMiddleware())

#############################END MIDDLEWARE#######################################


# Message CAN use only one keyboard !!!

# base command "start", dp.message - catch specific message from user. This example we use start command
@router.message(CommandStart())
async def cmd_start(message: Message):  # first param is message from user
    # "reply" is straight answer to message from user.
    # add keyboard after answer with "reply_markup"
    await message.reply(f'Hello! User.id: {message.from_user.id}, UserName: {message.from_user.first_name}', reply_markup=main_inline_menu,)


# base command "help"
@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('I can help you!', reply_markup=main_reply_menu)

# F.text - filter by text, if user write "How are you" in message bot will answer "Normally"
@router.message(F.text == 'How are you?')
async def cmd_how_are_you(message: Message):
    await message.answer('Normally', reply_markup=await keyboard_cars())  # add keyboard by builder

# func create keyboard that use callbacks
@router.message(F.text == "Callback")
async def cmd_callback(message: Message):
    await message.answer('Callbacks', reply_markup=main_callback_menu)

# F.photo - filter by photo
@router.message(F.photo)
async def send_photo(message: Message):
    await message.answer(f'ID Photo: {message.photo[-1].file_id}') # [-1] - the best quality the photo

# command "get_photo", answer with photo that we get from "send_photo" command
@router.message(Command('get_photo'))
async def cmd_get_photo_from_send_photo(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAMHZzxWWEv_bl9GPt0KiMUyh1jEVNUAAnrjMRshsOBJN9QAAVQtph17AQADAgADeQADNgQ', caption="Photo")

# command "get_photo_from_site", answer with photo that we get from site
@router.message(Command('get_photo_from_site'))
async def cmd_get_photo_from_site(message: Message):
    await message.answer_photo(photo='https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png', caption="Photo")


@router.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery ):
    # callback can be answered because need to use answer everything
    # show alert - open window that show text
    await callback.answer('You select callback', show_alert=True)

    # before or after we can send answer to user
    # to change same as message we can use edit_<type> functions
    await callback.message.edit_text('catalog', reply_markup=await inline_keyboard_cars())



###################################FSM#######################
@router.message(Command('reg'))
async def cmd_reg_name(message: Message, state: FSMContext):
    # use it before user should enter name
    await state.set_state(Reg.name)  # set name state
    await message.answer('Введите ваше имя')


@router.message(Reg.name)  # catch name of user to second step
async def reg_number(message: Message, state: FSMContext):
    # update name of Reg state obj
    await state.update_data(name=message.text)
    # set new state by number
    await state.set_state(Reg.number)
    await message.answer('Number: ')

@router.message(Reg.number) # catch number
async def reg_smth(message: Message, state: FSMContext):
    # update number of Reg state obj
    await state.update_data(number=message.text)
    # data - data (dict) of Reg obj (number and name)
    data = await state.get_data()
    # logic for save ...

    await message.answer(f'Thanks {data["name"]}, your number: {data["number"]} ')
    # clear Reg after save data to database
    await state.clear()

#############################END FSM################################