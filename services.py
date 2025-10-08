class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, name):
        if any(user['name'].lower() == name.lower() for user in self.users):
            raise ValueError(f'Имя пользователя {name} уже существует')
        self.users.append({'name': name})

    def get_users(self):
        return self.users
