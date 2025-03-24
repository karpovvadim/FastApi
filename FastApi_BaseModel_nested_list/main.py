from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
 
class Person(BaseModel):
    name: str
    languages: list = []
 
app = FastAPI()
 
@app.get("/")
def root():
    return FileResponse("public/index.html")
 
@app.post("/hello")
def hello(person: Person):
    print(person)
    return {"message": f"Name: {person.name}. Languages: {person.languages}"}
