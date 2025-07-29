from fastapi import FastAPI

app = FastAPI()

@app.get("/deneme")
def health_check():
    return {"status": "ok"}
