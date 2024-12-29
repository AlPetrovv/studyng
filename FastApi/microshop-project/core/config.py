import os
from pathlib import Path

#
# Base class for settings
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent  # microshop-project


class Status(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=os.path.join(BASE_DIR, "core/envs/status.env")
    )


class Settings(BaseSettings):
    """Can load env file"""

    api_v1_prefix: str = "/api/v1"
    db_url: str = f"sqlite+aiosqlite:///{BASE_DIR}/shop.sqlite3"
    debug: bool = False
    db_echo: bool = False


class DevSettings(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    db_url: str = f"sqlite+aiosqlite:///{BASE_DIR}/shop.sqlite3"
    debug: bool = True
    db_echo: bool = True


class TestSettings(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    db_url: str = f"sqlite+aiosqlite:///{BASE_DIR}/shop_test.sqlite3"
    debug: bool = False
    db_echo: bool = False


# status_settings = Status()
# settings_map = {"dev": DevSettings, "test": TestSettings, "prod": Settings}
# settings = settings_map[status_settings.STATUS]()

settings = DevSettings()
