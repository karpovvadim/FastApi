from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
 
app = FastAPI()
 
 
@app.get("/")
def root():
    return FileResponse("public/index.html")
 
 
@app.post("/postdata")
def postdata(username: str = Form(default ="Undefined", min_length=2, max_length=20), 
            userage: int =Form(default=18, ge=18, lt=111)):
    return {"name": username, "age": userage}
