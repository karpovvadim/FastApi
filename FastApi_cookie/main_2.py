from fastapi import FastAPI
from fastapi.responses import JSONResponse
from datetime import datetime
 
app = FastAPI()
 
 
@app.get("/")
def root():
    now = datetime.now()    # получаем текущую дату и время
    response = JSONResponse(content={"message": "куки установлены"})
    response.set_cookie(key="last_visit", value=now)
    return  response
