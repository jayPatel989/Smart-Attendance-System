# Smart Attendance System (Face Recognition)

A Smart Attendance System that uses **face recognition** to automatically mark attendance in real time.  
The system is built using **Python, OpenCV, Dlib, Flask, and SQLite**, and provides a secure web-based dashboard for managing attendance records.

This project eliminates the need for manual attendance and reduces proxy attendance by using facial recognition technology.

---

## Features

- Face registration using camera
- Real-time face recognition
- Automatic attendance marking
- Secure single-admin login
- Web-based dashboard
- Attendance records stored in SQLite database
- Browser-based live camera feed
- Start / Stop camera control from web interface

---

## Technology Stack

- **Programming Language:** Python  
- **Computer Vision:** OpenCV, Dlib  
- **Web Framework:** Flask  
- **Database:** SQLite  
- **Frontend:** HTML, CSS 

---

## How the System Works

1. **Admin Login**
   - Only the admin can access the system.
   - Login is required to open the dashboard.

2. **Face Registration**
   - Admin registers a new person by entering a name.
   - The camera captures multiple face images.
   - Images are stored in the `known_faces` directory.

3. **Attendance Recognition**
   - Camera detects and recognizes faces in real time.
   - If a face matches a registered person, attendance is marked automatically.
   - Attendance is saved with date and time.

4. **Dashboard**
   - Live camera feed displayed in browser.
   - Attendance records shown in a table.
   - Camera can be started and stopped using buttons.

---

## Installation & Setup

1. Clone the repository:
git clone https://github.com/jayPatel989/Smart-Attendance-System

2. Navigate to the project directory:

3. Install required Python libraries:
pip install -r requirements.txt

4. For first time only, run db_creation.py file from database/ folder to create an attendance database (If you want, change username and password from this file before running it):

5. Run the application (app.py):

6. Open the browser by clicking on the link:

---

## Important Notes

- This project is designed for **local system use**.
- The camera is controlled by OpenCV on the backend.
- The browser only displays the video stream.
- Only one admin is supported (single-user system).

---

## Use Cases

- Schools and colleges
- Training institutes
- Offices
- Labs and workshops

---

## Future Enhancements

- Multiple admin roles
- Cloud database support
- CSV export of attendance
- Improved face recognition accuracy
- Mobile-friendly UI

---

## Author

**Jay Patel**

---

## Disclaimer

This project is developed for academic and learning purposes.
