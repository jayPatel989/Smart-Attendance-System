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
- Attendance analytics with visual graphs
- Browser-based live camera feed (bonus feature)
- Start / Stop camera control from web interface

---

## Technology Stack

- **Programming Language:** Python  
- **Computer Vision:** OpenCV, Dlib  
- **Web Framework:** Flask  
- **Database:** SQLite  
- **Frontend:** HTML, CSS  
- **Data Visualization:** Matplotlib  

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
   - Graph showing attendance count per person.
   - Camera can be started and stopped using buttons.

5. **Analytics**
   - Attendance data is analyzed using SQLite queries.
   - Visual graphs are generated using Matplotlib.

---

## Project Structure

