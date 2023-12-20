# student_server.py
import os
import bluetooth
import face_recognition
import cv2
import requests
import pandas as pd

def load_student_images(student_folder):
    student_images = {}
    for filename in os.listdir(student_folder):
        if filename.endswith(".jpg"):
            student_name = os.path.splitext(filename)[0]
            student_image_path = os.path.join(student_folder, filename)
            student_image = face_recognition.load_image_file(student_image_path)
            student_images[student_name] = face_recognition.face_encodings(student_image)[0]
    return student_images

def detect_teacher_bluetooth():
    nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True, lookup_class=True, device_id=-1)

    print("Searching for nearby Bluetooth devices...")

    # Look for the teacher's Bluetooth device (replace with your logic)
    teacher_device_name = "Redmi 9"  # Replace with the actual name of the teacher's device
    teacher_device_address = None

    for addr, name, _ in nearby_devices:
        if name == teacher_device_name:
            teacher_device_address = addr
            break

    if teacher_device_address:
        print(f"Teacher's Bluetooth found at address {teacher_device_address}")

        # Define student folder
        student_folder = 'C:/Users/vishv/OneDrive/Documents/pythonProject4/image'  # Replace with the actual path to the student images folder

        # Load known student images
        known_student_images = load_student_images(student_folder)

        # Capture video from default camera
        cap = cv2.VideoCapture(0)

        # Create an empty attendance dataframe
        attendance_data = {"Student": [], "Status": []}

        while True:
            ret, frame = cap.read()
            # Find all face locations and face encodings in the current frame
            face_locations = face_recognition.face_locations(frame)
            face_encodings = face_recognition.face_encodings(frame, face_locations)

            for face_encoding in face_encodings:
                # Compare the face encoding with the known student images
                for student_name, student_encoding in known_student_images.items():
                    match = face_recognition.compare_faces([student_encoding], face_encoding)[0]
                    if match:
                        name = student_name
                        status = "Present"
                        break
                else:
                    name = "Unknown"
                    status = "Absent"

                # Append the attendance data
                attendance_data["Student"].append(name)
                attendance_data["Status"].append(status)

            # Display the resulting frame
            cv2.imshow('Video', frame)

            # Break the loop if 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the camera and close OpenCV
        cap.release()
        cv2.destroyAllWindows()

        # Send attendance data to the teacher's server
        send_attendance_data(attendance_data)

    else:
        print("Teacher's Bluetooth not found")

def send_attendance_data(attendance_data):
    # Specify the teacher's server URL
    server_url = "http://127.0.0.1:5000/"

    # Send attendance data to the server
    response = requests.post(server_url, json=attendance_data)

    if response.status_code == 200:
        print("Attendance data sent successfully")
    else:
        print("Failed to send attendance data")

if __name__ == "__main__":
    detect_teacher_bluetooth()
