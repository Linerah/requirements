class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    @staticmethod
    def create_user(database, username, email, password):
        user = User(username, email, password)
        user_document = user.convert_json()
        collection = database.db.users
        print(user_document)
        collection.insert_one(user_document)
        return user_document
    
    @staticmethod
    def get_users(database):
        collection = database.db.users
        users = collection.find()
        return list(users)

    @staticmethod
    def get_user(database, username):
        collection = database.db.users
        user = collection.find({'username': username})
        return list(user)

    #Getters
    def get_username(self): return self.username
    def get_email(self): return self.email
    def get_password(self): return self.password

    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}"

    def convert_json(self):
        return {"username": self.username, "email": self.email, "password": self.password}