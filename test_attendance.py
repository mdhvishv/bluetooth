# test_attendance.py
from attendance import mark_attendance

def test_mark_attendance():
    result = mark_attendance("test", "1234")
    print(result)
    assert "Attendance marked successfully" in result

if __name__ == "__main__":
    test_mark_attendance()
