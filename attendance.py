# attendance.py
import requests
from auth import authenticate_user
from bluetooths import detect_bluetooth_devices
from face_recognition_module import recognize_face, capture_face
import face_recognition
def mark_attendance(username, password):
    # Authenticate user
    if not authenticate_user(username, password):
        return "Authentication failed. Please check your credentials."

    # Detect Bluetooth devices
    detect_bluetooth_devices()

    # Capture a face image for recognition
    capture_face("face_to_recognize.jpg")

    # Known faces (replace with actual face encodings)
    known_faces = [
        # Face encoding for known person 1
        face_recognition.face_encodings(face_recognition.load_image_file("C:/Users/vishv/OneDrive/Documents/pythonProject4/madhav.jpg"))[0],
        # Face encoding for known person 2
        face_recognition.face_encodings(face_recognition.load_image_file("C:/Users/vishv/OneDrive/Documents/pythonProject4/richa.jpg"))[0],
        # Add more known faces as needed
    ]


    # Recognize face for attendance
    if recognize_face("face_to_recognize.jpg", known_faces):
        # Send attendance data to the server
        attendance_data = {"username": username, "status": "present"}  # Modify as needed
        response = requests.post("http://127.0.0.1:5000/record_attendance", json=attendance_data)

        if response.status_code == 200:
            return "Attendance marked successfully."
        else:
            return f"Failed to mark attendance. Server responded with status code {response.status_code}."
    else:
        return "Face not recognized. Attendance marking failed."