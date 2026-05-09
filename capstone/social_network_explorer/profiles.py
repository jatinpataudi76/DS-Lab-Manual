class ProfileManager:
    def __init__(self):
        self.users = {}  # hash map: user_id -> profile

    def add_user(self, user_id, name, age, interests):
        if user_id in self.users:
            print("User already exists!")
            return
        self.users[user_id] = {
            "name": name,
            "age": age,
            "interests": interests  # list of strings
        }
        print(f"User '{name}' added.")

    def get_profile(self, user_id):
        if user_id not in self.users:
            print("User not found!")
            return None
        return self.users[user_id]

    def update_profile(self, user_id, name=None, age=None, interests=None):
        if user_id not in self.users:
            print("User not found!")
            return
        if name:      self.users[user_id]["name"] = name
        if age:       self.users[user_id]["age"] = age
        if interests: self.users[user_id]["interests"] = interests
        print(f"Profile {user_id} updated.")

    def show_profile(self, user_id):
        p = self.get_profile(user_id)
        if p:
            print(f"ID: {user_id} | Name: {p['name']} | Age: {p['age']} | Interests: {p['interests']}")