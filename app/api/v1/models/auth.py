from werkzeug.security import generate_password_hash

users = [{
    "is_admin": True,
    "email": "test@adminmail.com",
    "name": "test",
    "password": "pass",
    "user_id": 1,
    "username": "tester"
    }]

class UserModel():
    def __init__(self):
        self.users = users

    def add_user(self, name, email, usrnm, pswrd, is_admin):
        self.user_id = len(self.users)+1
        self.password = pswrd
        #generate_password_hash(pswrd, method='pbkdf2:sha256', salt_length=12)

        user = {
            "user_id": self.user_id,
            "name": name,
            "email": email,
            "username": usrnm,
            "password": self.password,
            "is_admin": False
            }

        self.users.append(user)

        return user

    def get_all(self):
        return self.users