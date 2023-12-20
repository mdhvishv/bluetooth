# auth.py
from models import User

def authenticate_user(username, password):
    # Replace this with your authentication logic
    valid_user = User("test", "1234")
    return username == valid_user.username and password == valid_user.password
