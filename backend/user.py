class User:
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    #Getters
    def get_id(self): return self.id
    def get_username(self): return self.username
    def get_email(self): return self.email
    def get_password(self): return self.password

    def __str__(self):
        return f"User(ID: {self.id}, Username: {self.username}, Email: {self.email}"