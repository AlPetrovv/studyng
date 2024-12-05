import uvicorn

from fastapi import FastAPI
from items.views import router as items_router
from users.views import router as users_router

app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)


@app.get("/")
def hello_index() -> dict:
    return {"message": "Hello World!"}


@app.get("/hello/")
def hello(name: str = "World") -> dict:
    name = name.strip().title()
    return {"message": f"Hello {name}!"}


@app.post("/calculate/")
def add(a: int, b: int):
    return {"sum": a + b}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
