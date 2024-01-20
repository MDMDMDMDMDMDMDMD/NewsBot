import random

from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import Command, CommandObject, CommandStart
from webscrapers import web_scraper

from keyboards import reply

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Hello, AIOgram 3.x", reply_markup=reply.main)


@router.message(Command(commands=["rn", "random-number"])) # /rn 1-100
async def get_random_number(message: Message, command: CommandObject):
    a, b = [int(n) for n in command.args.split("-")]
    rnum = random.randint(a, b)

    await message.reply(f"Random number: {rnum}")


# @router.message(Command("test"))
# async def test(message: Message, bot: Bot):
#     await bot.send_message(message.chat.id, "test")
@router.message(Command("test"))
async def test(message: Message, bot: Bot):
    await bot.send_message(message.chat.id, "Running web scrapers...")

    # Вызываем функции из файла webscrapers.py
    web_scraper.scraper_3dnews()
    web_scraper.scraper_habr()
    web_scraper.scraper_ixbt()
    web_scraper.scraper_overclockers()
    web_scraper.scraper_rozetked()

    await bot.send_message(message.chat.id, "Web scrapers completed!")
