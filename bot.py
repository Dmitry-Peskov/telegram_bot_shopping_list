import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.methods import DeleteWebhook
from aiogram.client.default import DefaultBotProperties

from settings import Config
import handlers


dp = Dispatcher()
dp.include_router(handlers.commands)
properties = DefaultBotProperties(parse_mode=ParseMode.HTML)


async def main() -> None:
    bot = Bot(
        token=Config.Bot.TOKEN,
        default=properties
    )
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(
        bot,
        allowed_updates=dp.resolve_used_update_types()
    )


if __name__ == "__main__":
    logging.basicConfig(
        level=Config.Logging.LEVEL,
        stream=sys.stdout,
        format=Config.Logging.FORMAT
    )
    asyncio.run(main())
