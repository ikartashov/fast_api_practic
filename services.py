import database


class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, name):
        return database.add_user(name)

    def get_users(self):
        return database.get_users()
