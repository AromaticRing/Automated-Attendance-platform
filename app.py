from flask import Flask, render_template, request, jsonify
import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime
import base64

app = Flask(__name__)

# Load images and encode them
path = 'dataset'
images = []
classNames = []
mylist = os.listdir(path)
for cl in mylist:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encoded_faces = face_recognition.face_encodings(img)
        if encoded_faces:
            encodeList.append(encoded_faces[0])
    return encodeList

encoded_face_train = findEncodings(images)

# Attendance marking function
def markAttendance(name):
    with open('Attendance.csv', 'a+') as f:
        f.seek(0)
        myDataList = f.readlines()
        nameList = [line.split(',')[0] for line in myDataList]

        if name not in nameList:
            now = datetime.now()
            time = now.strftime('%I:%M:%S %p')
            date = now.strftime('%d-%B-%Y')
            f.write(f'{name}, {time}, {date}\n')

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture', methods=['POST'])
def capture():
    data = request.json['image']
    image_data = base64.b64decode(data.split(',')[1])
    np_arr = np.frombuffer(image_data, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faces_in_frame = face_recognition.face_locations(imgS)
    encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)

    for encode_face, faceloc in zip(encoded_faces, faces_in_frame):
        matches = face_recognition.compare_faces(encoded_face_train, encode_face)
        faceDist = face_recognition.face_distance(encoded_face_train, encode_face)
        matchIndex = np.argmin(faceDist)

        if matches[matchIndex]:
            name = classNames[matchIndex].lower()
            markAttendance(name)
            return jsonify({"name": name})
    return jsonify({"name": "Unknown"})

@app.route('/view_attendance', methods=['GET'])
def view_attendance():
    with open('Attendance.csv', 'r') as f:
        data = f.read()
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

