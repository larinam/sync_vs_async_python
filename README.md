# Comparing Synchronous vs. Asynchronous Python with Locust and FastAPI

This project demonstrates the performance differences between synchronous and asynchronous setups using FastAPI in respective modes, tested with Locust.

## Running
You can configure the number of available threads for the sync setup directly in `sync.py`.

```
pip install -r requirements.txt
uvicorn sync:app --host 0.0.0.0 --port 8001 --workers 1
uvicorn async:app --host 0.0.0.0 --port 8000 --workers 1
locust
```

To run the test, open Locust at [http://0.0.0.0:8089/](http://0.0.0.0:8089/) and start the simulation.

## NB
Note that the performance of Locust itself might be a limiting factor. Ensure that Locust does not exceed 100% CPU usage, as it may not be able to generate maximum load on the applications. For this test, the optimal number of users was around 5000.

## Conclusion
From the outcomes observed, at ~800 requests per second, there was not much difference in performance between the synchronous and asynchronous configurations. There was perhaps a 50% higher CPU usage observed in the synchronous setup (20% vs. 30% of one core) and a memory consumption difference (80 MB vs. 120 MB) with the asynchronous setup being more efficient.



