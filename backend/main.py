from fastapi import FastAPI

from core.config import settings
from db.session import engine
from db.base_class import Base
#from db.base import Base


def create_table():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
#    create_table()
    return app

app = start_application()

"""""
@app.get("/")
def hello():
    return {"msg": "Starting my student's portal project"}
"""""
