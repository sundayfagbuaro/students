import os
from urllib.request import localhost

from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'

load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_TITLE: str = "Student Portal"
    PROJECT_VERSION: str = "1.0.0"


    MYSQL_USER: str = os.getenv("MYSQL_USER")
    MYSQL_USER_PASSWORD: str = os.getenv("MYSQL_USER_PASSWORD")
    MYSQL_HOST: str = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_PORT: int = os.getenv("MYSQL_PORT", 3306)
    MYSQL_DATABASE: str = os.getenv("MYSQL_DATABASE")
    DATABASE_URL: str =f"mysql+pymysql://{MYSQL_USER}:{MYSQL_USER_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"


settings = Settings()