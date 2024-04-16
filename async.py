from fastapi import FastAPI
import asyncio

app = FastAPI()


@app.get("/async")
async def async_root():
    await asyncio.sleep(1)  # Simulating an async I/O operation
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
