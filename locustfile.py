from locust import HttpUser, task, between


class AsyncUser(HttpUser):
    host = "http://localhost:8000"
    wait_time = between(1, 2)

    @task
    def get_async(self):
        self.client.get("/async")


class StandardUser(HttpUser):
    host = "http://localhost:8001"
    wait_time = between(1, 2)

    @task
    def get_standard(self):
        self.client.get("/standard")
