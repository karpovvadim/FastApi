from fastapi import FastAPI, Body
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
def root():
    return FileResponse("public/index.html")


@app.post("/hello")
def hello(name: str = Body(embed=True, min_length=3, max_length=20),
          age: int = Body(embed=True, ge=18, lt=111)):
    # def hello(data=Body()):
    #   name = data["name"]
    #   age = data["age"]
    return {"message": f"{name}, ваш возраст - {age}"}
