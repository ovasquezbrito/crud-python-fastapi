from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"data":{"name":"Oduber vasquez"}}
