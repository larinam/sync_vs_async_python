# Compare Sync vs Async Python with Locust and FastAPI in sync and asyncio modes.

The number of available threads can be configured directly inside `sync.py`.

```
pip install -r requirements.txt
uvicorn sync:app --host 0.0.0.0 --port 8001 --workers 1
uvicorn async:app --host 0.0.0.0 --port 8000 --workers 1
locust
```

Open locust and run test: http://0.0.0.0:8089/.
