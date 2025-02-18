from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

# Creating instance of app
app = FastAPI()

# Creating User model
class User(BaseModel):
    id: int
    name: str
    email: str
    password: str

# Dictionary to store users - Temporary
users_db: Dict[int, User] = {}