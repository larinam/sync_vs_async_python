import anyio
from fastapi import FastAPI
import time

app = FastAPI()


@app.on_event("startup")
async def startup():
    limiter = anyio.to_thread.current_default_thread_limiter()
    limiter.total_tokens = 800


@app.get("/standard")
def standard_root():
    time.sleep(1)  # Simulating a blocking I/O operation
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, workers=1)
