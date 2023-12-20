# test_auth.py
from auth import authenticate_user

def test_authentication():
    assert authenticate_user("test", "1234") is True
    assert authenticate_user("invalid", "password") is False

if __name__ == "__main__":
    test_authentication()
