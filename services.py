import database


class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, name):
        return database.add_user(name)

    def get_users(self):
        return database.get_users()

    def get_user_by_id(self, user_id):
        return database.get_user_by_id(user_id)

    def update_user(self, user_id, new_name):
        return database.update_user(user_id, new_name)

    def delete_user(self, user_id):
        return database.delete_user(user_id)
