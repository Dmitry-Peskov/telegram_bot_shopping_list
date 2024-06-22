from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from core import models
from settings import Config


class DataBase:
    def __init__(self):
        self.__engine = create_async_engine(url=Config.DataBase.DSN,
                                            echo=Config.DataBase.ECHO,
                                            pool_size=Config.DataBase.POOL_SIZE,
                                            max_overflow=Config.DataBase.MAX_OVERFLOW,
                                            )
        self.__session = async_sessionmaker(self.__engine,
                                            expire_on_commit=Config.DataBase.EXPIRE_ON_COMMIT,
                                            autoflush=Config.DataBase.AUTOFLUSH
                                            )

    def add_new_user(self, user: models.User) -> None:
        """
        Зарегистрировать нового участника в системе

        :param user: пользователь Telegram
        :return:
        """
        async with self.__session() as session:
            async with session.begin():
                action = models.Action(
                    user_id=user.telegram_id,
                    message="Регистрация нового пользователя",
                    details=str(user)
                )
                session.add(user)
                session.add(action)

    async def this_user_exists(self, telegram_id: int) -> bool:
        """
        Проверит зарегистрирован ли пользователь в системе по его Telegram ID

        :param telegram_id: ID пользователя в Telegram
        :return: True если зарегистрирован, иначе False
        """
        async with self.__session() as session:
            async with session.begin():
                user = await session.get(models.User, {"telegram_id": telegram_id})
                result = False if user is None else True
                return result


DBHelper = DataBase()
