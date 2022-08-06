from typing import Any

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root() -> Any:
    return {"message": "Hello World"}
