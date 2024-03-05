from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello world"}


@app.post("/")
async def post():
    return {"message": "Hello from post route"}
