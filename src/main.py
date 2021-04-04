from fastapi import FastAPI

app = FastAPI()


@app.get("/user/")
def home():
    return {"Hello": "wgolad"}
