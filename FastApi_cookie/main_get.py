from fastapi import FastAPI, Cookie
 
app = FastAPI()
 
@app.get("/")
def root(last_visit: str | None = Cookie(default=None)):
    if last_visit == None:
        return {"message": "Это ваш первый визит на сайт"}
    else:
        return  {"message": f"Ваш последний визит: {last_visit}"}
