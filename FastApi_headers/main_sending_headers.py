from fastapi import FastAPI, Response
 
app = FastAPI()
 
@app.get("/")
def root():
    data = "Hello METANIT.COM"
    return Response(content=data, media_type="text/plain", headers={"Secret-Code" : "123"})
