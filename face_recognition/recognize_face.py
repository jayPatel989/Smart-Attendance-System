import cv2
import os
import sys
import numpy as np

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from face_recognition.face_utils import detect_faces, get_face_encoding, load_known_faces
from database.db_utils import mark_attendance_db

known_encodings, known_names = load_known_faces()
def recognize_face(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detect_faces(gray)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        encoding = get_face_encoding(frame, gray, (x, y, w, h))
        distances = np.linalg.norm(known_encodings - encoding, axis=1)
        min_distance = np.min(distances)

        if min_distance < 0.6:
            name = known_names[np.argmin(distances)]
            mark_attendance_db(name)
        else:
            name = "Unknown"

        cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)