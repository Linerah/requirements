#Load testing using locust

from locust import HttpUser, task, between

class User(HttpUser):

    wait_time = between(1, 5)

    #Simulating login
    def on_start(self):
        self.client.post("/login", data={"username":"kevlinelcaballote", "password":"a12341231"})
    
    @task
    def main_page(self):
        self.client.get("/")
    
    #Simulating opening schedule.
    @task
    def schedule(self):
        self.client.get("/schedule")

    