import os
import logging
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Config:
    @dataclass(frozen=True)
    class Bot:
        TOKEN: str = os.getenv("BOT_API_TOKEN")

    @dataclass(frozen=True)
    class DataBase:
        DSN: str = f"sqlite+aiosqlite:///{os.getcwd()}\\db.sqlite3"
        POOL_SIZE: int = 20
        MAX_OVERFLOW: int = 10
        ECHO: bool = True
        AUTOFLUSH: bool = False
        AUTOCOMMIT: bool = False
        EXPIRE_ON_COMMIT: bool = False

    @dataclass(frozen=True)
    class Developer:
        TELEGRAM_ID: int = int(os.getenv("DEVELOPER_TELEGRAM_ID"))
        TELEGRAM_URL: str = os.getenv("DEVELOPER_TELEGRAM_URL")
        GITHUB_URL: str = os.getenv("DEVELOPER_GITHUB_URL")
        VK_URL: str = os.getenv("DEVELOPER_VK_URL")

    @dataclass(frozen=True)
    class Logging:
        FORMAT: str = "%(asctime)s | %(levelname)s | %(name)s | %(filename)s | %(funcName)s | %(lineno)d | %(message)s"
        LEVEL: int = logging.INFO
