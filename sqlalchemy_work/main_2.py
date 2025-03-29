from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import Column, Integer, String

from fastapi import FastAPI

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})


class Base(DeclarativeBase): pass


class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer, )


SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()

# Для обновления объекта достаточно изменить значения его атрибутов и затем
# вызвать у объекта Session метод commit() для применения изменений

# получаем один объект, у которого имя - Tom
tom = db.query(Person).filter(Person.id == 1).first()
print(f"{tom.id}.{tom.name} ({tom.age})")
# 1.Tom (42)

# изменениям значения
tom.name = "Tomas"
tom.age = 22

db.commit()  # сохраняем изменения

# проверяем, что изменения применены в бд - получаем один объект, у которого
# имя - Tomas
tomas = db.query(Person).filter(Person.id == 1).first()
print(f"{tomas.id}.{tomas.name} ({tomas.age})")
# 1.Tomas (22)

# Для удаления у объекта Session применяется метод delete(), в который
# передается удаляемый объект
# bob = db.query(Person).filter(Person.id==2).first()
# db.delete(bob)  # удаляем объект
# db.commit()     # сохраняем изменения
