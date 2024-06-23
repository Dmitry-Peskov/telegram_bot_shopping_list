import logging
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from core.models import User, Action
from core.database import DBHelper


logger = logging.getLogger(__name__)
commands = Router(name=__name__)


@commands.message(CommandStart())
async def start(message: Message):
    user_id = message.from_user.id
    user_exists = await DBHelper.this_user_exists(user_id)
    if not user_exists:
        logger.info(f"Пользователь с ID = {user_id} не обнаружен в системе")
        user = User(
            telegram_id=user_id,
            fullname=message.from_user.full_name,
            nickname=message.from_user.username
        )
        await DBHelper.add_new_user(user)
        logger.info(f"Пользователь с ID = {user_id} был зарегистрирован")
    action = Action(
        user_id=user_id,
        message="Вызвана команда /start",
        details=""
    )
    await DBHelper.add_action(action)
    logger.info(f"Пользователь с ID = {user_id} вызвал /start")
    await message.delete()
