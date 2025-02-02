import os
from pathlib import Path

from pydantic import BaseModel

#
# Base class for settings
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent  # microshop-project


DB_PATH = BASE_DIR / "shop.sqlite3"


class Status(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=os.path.join(BASE_DIR, "core/envs/status.env")
    )


class DBSettings(BaseModel):
    url: str = f"sqlite+aiosqlite:///{DB_PATH}"
    echo: bool = True


class Settings(BaseSettings):
    """Can load env file"""

    api_v1_prefix: str = "/api/v1"
    debug: bool = False
    db_settings: DBSettings = DBSettings()


class DevSettings(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    debug: bool = True
    db_settings: DBSettings = DBSettings()


class TestSettings(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    debug: bool = False
    db_settings: DBSettings = DBSettings()


# status_settings = Status()
# settings_map = {"dev": DevSettings, "test": TestSettings, "prod": Settings}
# settings = settings_map[status_settings.STATUS]()

settings = DevSettings()
