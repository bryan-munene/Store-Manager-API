from werkzeug.security import generate_password_hash, check_password_hash

users = [{
    "is_admin": True,
    "email": "test@adminmail.com",
    "name": "test",
    "password": "pbkdf2:sha256:50000$q8g2do0iUoJQ$5404483ab74e080c67243542d610e49690fe05ebffcd538e2775319f9fbb70f9",
    "user_id": 1,
    "username": "tester"
    }]

class UserModel():
    def __init__(self):
        self.users = users

    def add_user(self, name, email, usrnm, pswrd, is_admin):
        self.user_id = len(self.users)+1
        self.password = generate_password_hash(pswrd, method='pbkdf2:sha256', salt_length=12)

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

    def get_user_by_email(self, email):
        if len(users) > 0:
            for user in users:
                user_email = user.get('email')

                if email == user_email:
                    return user

    def check_password(self, user_password, password):
        return check_password_hash(user_password, password)