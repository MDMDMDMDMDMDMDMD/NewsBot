from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

links = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="YouTube", url="https://www.youtube.com"),
            InlineKeyboardButton(text="Telegram", url="tg://resolve?domain=telegram")
        ]
    ]
)