# server.py
from flask import Flask, request

app = Flask(__name__)

@app.route('/record_attendance', methods=['POST'])
def record_attendance():
    data = request.json
    print(f"Received attendance data: {data}")
    # Add logic to record attendance in a database or file
    return "Attendance recorded successfully"

if __name__ == "__main__":
    app.run(debug=True)
