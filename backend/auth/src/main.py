from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.api_v1 import router as api_v1_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup app
    yield
    # shutdown app


app = FastAPI(
    lifespan=lifespan,
)
app.include_router(router=api_v1_router)
