from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel


class Company(BaseModel):
    name: str


class Person(BaseModel):
    name: str
    company: Company


app = FastAPI()


@app.get("/")
def root():
    return FileResponse("public/index.html")


@app.post("/hello")
def hello(person: Person):
    print (person)
    return {"message": f"{person.name} ({person.company.name})"}
