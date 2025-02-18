from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

# Creating instance of app
app = FastAPI()

# Test the app
@app.get('/')
def main_app():
    return "Hi from the FastAPI App"

# Creating User model
class User(BaseModel):
    user_id: int
    name: str
    # email: str
    # password: str

# Dictionary to store users - Temporary
users_db: Dict[int, User] = {}

# This Method uses Params
# # Route to add a new user
# @app.post('/users/')
# def add_users(user_id: int, name: str):
#     if user_id in users_db:
#         raise HTTPException(status_code=400, detail="User Already Exists.")
#     user = User(user_id, name)
#     users_db[user_id] = user
#     return {
#         "message": "User Added", "user": user
#     }

# Route to add a user
@app.post('/users/')
def add_users_json(user: User):
    if user.user_id in users_db:
        raise HTTPException(status_code=400, detail="User Already Exists.")
    users_db[user.user_id] = user
    return {
        "message": "User Added", 
        "user": user
    }