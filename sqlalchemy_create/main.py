from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String

from fastapi import FastAPI

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# создание движка
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
print(engine)


# При работе с другими СУБД достаточно указать только адрес подключения:
# engine = create_engine(SQLALCHEMY_DATABASE_URL)

# создаем базовый класс для моделей
Base = declarative_base()
# class Base(DeclarativeBase): pass


# создаем модель, объекты которой будут храниться в бд
class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer, )

    print("2 -", __tablename__)


# создаем таблицы
Base.metadata.create_all(bind=engine)

# приложение, которое ничего не делает
app = FastAPI()
