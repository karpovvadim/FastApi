from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import Column, Integer, String

from fastapi import FastAPI

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})


# создаем модель, объекты которой будут храниться в бд
class Base(DeclarativeBase): pass


class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer, )


# создаем таблицы
Base.metadata.create_all(bind=engine)

# создаем сессию подключения к бд
SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()

# создаем объект Person для добавления в бд
tom = Person(name="Tom", age=42)
db.add(tom)  # добавляем в бд
db.commit()  # сохраняем изменения
alice = Person(name="Alice", age=33)
kate = Person(name="Kate", age=28)
db.add_all([alice, kate])
db.commit()
print(tom.id, tom.name, tom.age)  # можно получить установленный id, name, age

# получение всех объектов
people = db.query(Person).all()
for p in people:
    print(f"{p.id}.{p.name} ({p.age})")

# Для получения одного объекта по id применяется метод get() класса Session
first_person = db.get(Person, 1)  # id = 1
print(f"метод get() {first_person.name} - {first_person.age}")

# Для фильтрации у объекта Query применяется метод filter()
people = db.query(Person).filter(Person.age > 30).all()
print("\nметод filter()")
for p in people:
    print(f"{p.id}.{p.name} ({p.age})")

# Для получения только одного объекта применяется метод first() класса Query
first = db.query(Person).filter(Person.id == 1).first()
print(f"метод first() {first.name} ({first.age})")

# Стоит отметить, что методы get() и first() возвращают None, если объект
# не найден. Поэтому при получении одиночного объекта желательно проверять
# его на значение None.

# приложение, которое ничего не делает
app = FastAPI()
