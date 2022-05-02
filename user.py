import hashlib
import re
import time


class User:
    def __init__(self, username, email, password, password_is_hashed=False, admin=False):
        if (
            (type(email) is not str)
            or (type(password) is not str)
            or (type(username) is not str)
        ):
            raise TypeError("email, password and username parameters must be strings")
        self.admin = admin
        self.set_email(email.strip())
        self.set_username(username.strip())
        self.usr_id = self.generate_user_ID()
        if password_is_hashed:
            self.password = password
        else:
            self.set_password(password.strip())

    #Getters
    def get_username(self): return self.username
    def get_email(self): return self.email
    def get_password(self): return self.password
    def __str__(self):
        return (
            f"Username: {self.username}\nEmail: {self.email}\nPassword: {self.password}\nRank: {self.admin}"
        )

    # Setters
    def set_email(self, email):
        if not self.check_valid_email(email):
            raise ValueError("Invalid email")
        self.email = email

    def set_password(self, password):
        if not self.check_valid_password(password):
            raise ValueError("Invalid password")
        self.password = self.hash_password(password)

    def set_username(self, username):
        if not self.check_valid_username(username):
            raise ValueError("Invalid username")
        self.username = username

    # Validity checks
    def check_valid_email(self, email):
        # Uses RFC 5322 email standard to check if an email is valid
        regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        if re.fullmatch(regex, email):
            return True
        return False

    def check_valid_password(self, password):
        # Min 8 chars, 1 letter, 1 number
        time.sleep(1)  # Make password verification slower to prevent brute force attack
        regex = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")
        if re.fullmatch(regex, password):
            return True
        return False

    def check_valid_username(self, username):
        # 3-20 alphanum chars and "." "_"
        regex = re.compile(r"[a-zA-Z0-9._]{3,20}$")
        if re.fullmatch(regex, username):
            return True
        return False
           
     # Generators
    def hash_password(self, password):
        # Hashes password and returns hash in hexadecimal format
        hashed_password = hashlib.sha512()
        hashed_password.update(password.encode("utf8"))
        return hashed_password.hexdigest()

    def generate_user_ID(self):
        # Generate unique user ID
        cur_time = str(time.time())
        hashed_time = hashlib.sha1()
        hashed_time.update(cur_time.encode("utf8"))
        return hashed_time.hexdigest()
        
    def to_json(self):
        # Returns a dictionary of the user's attributes
        return {
            "email": self.email,
            "password": self.password,
            "username": self.username,
            "usr_id": self.usr_id,
            "admin": self.admin,
        }

     # Compare
    def compare_password(self, password):
        # Checks if input password matches stored password
        if self.password == self.hash_password(password):
            return True
        return False

    # Mongo
    @staticmethod
    def create_user(database, username, email, password):
        user = User(username, email, password)
        user_document = user.to_json()
        collection = database.db.users
        print(user_document)
        collection.insert_one(user_document)
        return user
    
    @staticmethod
    def get_user(database, username):
        collection = database.db.users
        user_document = collection.find_one({'username': username})
        if user_document is None:
            return None
        return User(
            user_document["username"],
            user_document["email"],
            user_document["password"],
            True,
            user_document["admin"]
        )
    @staticmethod    
    def get_user_by_id(database, usr_id):
        collection = database.db.users
        user_document = collection.find_one({'usr_id': usr_id})
        if user_document is None:
            return None
        return User(
            user_document["username"],
            user_document["email"],
            user_document["password"],
            True,
            user_document["admin"]
        )
    @staticmethod
    def get_users(database):
        collection = database.db.users
        user_document = collection.find()
        if user_document is None:
            return None
        return user_document
    
    @staticmethod
    def update_user(database, usr_id, username, email, admin):
        collection = database.db.users
        collection.update_one( {"usr_id": usr_id}, {"$set": {"username": username, "email": email, "admin": admin}}) 

    @staticmethod
    def delete_user(database, usr_id):
        collection = database.db.users
        collection.delete_one({'usr_id': usr_id})