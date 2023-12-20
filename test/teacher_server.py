# teacher_server.py
from flask import Flask, request
import pandas as pd

app = Flask(__name__)

attendance_df = pd.DataFrame(columns=["Student", "Status"])

@app.route('/record_attendance', methods=['POST'])
def record_attendance():
    global attendance_df

    attendance_data = request.get_json()
    new_attendance_df = pd.DataFrame(attendance_data)

    attendance_df = pd.concat([attendance_df, new_attendance_df], ignore_index=True)

    # Save the attendance data to an Excel file
    attendance_df.to_excel("attendance.xlsx", index=False)

    return "Attendance marked successfully"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
