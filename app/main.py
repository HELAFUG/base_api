import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from core.models import db_helper
from api import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):

    yield
    await db_helper.dispose()


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
