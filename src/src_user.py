
# src/user.py

class User:
    def __init__(self, user_id, name, email, password, role):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.role = role

    def login(self):
        print(f"{self.name} logged in.")

    def logout(self):
        print(f"{self.name} logged out.")

    def update_profile(self, name=None, email=None):
        if name:
            self.name = name
        if email:
            self.email = email
        print(f"{self.name}'s profile updated.")
