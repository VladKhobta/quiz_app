from envparse import Env

from pydantic_settings import BaseSettings

env = Env()

DATABASE_URL = env.str(
    'DATABASE_URL',
    default='postgresql+asyncpg://postgres:postgres@127.0.0.1:5432/postgres'
)

APP_PORT = env.int(
    "APP_PORT",
    default=8000
)
