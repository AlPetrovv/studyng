import uvicorn
from fastapi import FastAPI
from setup import lifespan

from api.v1 import router as api_v1_router
from old.items.views import router as items_router
from old.users.views import router as users_router

app = FastAPI(lifespan=lifespan)
app.include_router(items_router)
app.include_router(users_router)
app.include_router(api_v1_router)


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
    uvicorn.run("main:app", reload=True, port=8001)
