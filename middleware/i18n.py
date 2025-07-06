from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Dict, Any
from utils.language import get_user_language, translate

class I18nMiddleware(BaseMiddleware):
    async def on_pre_process_message(self, message: Message, data: Dict[str, Any]):
        user_id = message.from_user.id
        lang = await get_user_language(user_id)
        data["i18n"] = lambda key: translate(key, lang)