from fastapi import FastAPI, Response, Path

# from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/users/{id}", status_code=200)
def users(response: Response, id: int = Path()):
    if id < 1:
        response.status_code = 400
        return {"message": "Incorrect Data"}
    return {"message": f"Id = {id}"}
