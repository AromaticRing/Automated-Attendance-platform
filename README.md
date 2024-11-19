# Automated Face Recognition Attendance System

This project is an AI-driven attendance system that uses face recognition to mark attendance. It is designed to simplify and automate attendance tracking in schools, workplaces, and events.

## Features
- Real-time face detection and recognition.
- Automated attendance recording and management.
- Support for multiple users with dynamic database updates.
- Easy-to-use interface for admin and attendees.

## How to Set Up

### Prerequisites
1. Python 3.7 or higher.
2. Install the following software/tools:
   - **pip** (Python package installer)
   - **OpenCV**
   - **Dlib**
   - **Face Recognition Library** (based on Dlib)
3. A webcam or external camera for capturing real-time video feed.

### Installation
1. Clone the repository:
   bash
   $ git clone https://github.com/your-repo/face-recognition-attendance.git
   $ cd face-recognition-attendance
   
2. Install dependencies:
   bash
   $ pip install -r requirements.txt
   
3. Configure the database (if applicable):
   - Set up an SQLite/MySQL database.

4. Train the model with user images:
   - Add user images to the `dataset` folder (create separate folders for each person, e.g., `dataset/person1`).

5. Start the application:
   bash
   $ python app.py

### Usage
1. Launch the application.
2. Register new attendees through the admin interface.
3. Use the camera feed to detect and log attendance in real time.
