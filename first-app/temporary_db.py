from typing import Dict

class User:
    def __init__(self, user_id: int, name: str):
        self.user_id = user_id
        self.name = name

    def __repr__(self):
        return f"User(user_id={self.user_id}, name='{self.name}')"

# Dictionary to store users
users_db: Dict[int, User] = {}

# Adding users to the dictionary
users_db[1] = User(1, "Alice")
users_db[2] = User(2, "Bob")

# Accessing users
print(users_db[1])  # Output: User(user_id=1, name='Alice')
print(users_db[2])  # Output: User(user_id=2, name='Bob')

# Checking if a user exists
if 3 in users_db:
    print("User exists")
else:
    print("User not found")  # Output: User not found
