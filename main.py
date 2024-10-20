from fastapi import FastAPI

from contextlib import asynccontextmanager

from database import create_tables, delete_tables
from router import router as task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load model
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова")
    yield
    # clean
    print("Выключение")


app = FastAPI(lifespan=lifespan)
app.include_router(task_router)
