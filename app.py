from fastapi import FastAPI

app = FastAPI(title="FastAPI Demo Project")

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI 🚀"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "query": q}
