import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Firebase authentication
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://gate-pass-system-c8536-default-rtdb.firebaseio.com/"
})

# Function to add a new student record
def add_student(ref, student_id, name, major, starting_year, total_attendance, standing, year, last_attendance_time):
    student_data = {
        "name": name,
        "major": major,
        "starting_year": starting_year,
        "total_attendance": total_attendance,
        "standing": standing,
        "year": year,
        "last_attendance_time": last_attendance_time
    }
    ref.child(student_id).set(student_data)

# Function to get a student record
def get_student(ref, student_id):
    return ref.child(student_id).get()

# Function to update a student record
def update_student(ref, student_id, updates):
    ref.child(student_id).update(updates)

# Function to delete a student record
def delete_student(ref, student_id):
    ref.child(student_id).delete()

# Main program
ref = db.reference('Students')

# Add new student record
add_student(ref, "321654", "Murtaza Hassan", "Robotics", 2017, 7, "G", 4, "2022-12-11 00:54:34")
add_student(ref, "0123", "Jac Mwas", "Computer Science", 2017, 0, "G", 4, "2022-12-11 00:54:34")
add_student(ref, "9876543", "Mwas Jac", "IOT", 2017, 0, "G", 4, "2022-12-11 00:54:34")
add_student(ref, "852741", "Emily Blunt", "Economics", 2021, 12, "B", 1, "2022-12-11 00:54:34")
add_student(ref, "963852", "Elon Musk", "Physics", 2020, 7, "G", 2, "2022-12-11 00:54:34")

# Get a student record
print(get_student(ref, "321654"))

# Update a student record
update_student(ref, "963852", {"total_attendance": 10, "year": 3})
print(get_student(ref, "963852"))

# Delete a student record
delete_student(ref, "852741")
