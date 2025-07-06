from aiogram import Router, types, F
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from utils.language import set_user_language, translate

router = Router()

@router.message(F.text == "/start")
async def cmd_start(message: Message):
    buttons = [
        InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru"),
        InlineKeyboardButton(text="🇺🇿 Ўзбекча", callback_data="lang_uz"),
        InlineKeyboardButton(text="🇰🇿 Қарақалпақша", callback_data="lang_kk")
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[btn] for btn in buttons])
    await message.answer(translate("choose_language", lang="ru"), reply_markup=keyboard)
    # Заменить "ru" на дефолтный язык, если нужно

@router.callback_query(F.data.startswith("lang_"))
async def set_language(callback: CallbackQuery):
    lang = callback.data.split("_")[1]
    await set_user_language(callback.from_user.id, lang)
    await callback.message.answer(translate("start", lang))
    await callback.answer()
