import time
from fastapi import FastAPI, Request

from src.router import news
from get_data_from_sites import get_data
app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

app.include_router(news.router)


@app.get("/")
def read_root():
    return {"message": "module 15"}

get_data()