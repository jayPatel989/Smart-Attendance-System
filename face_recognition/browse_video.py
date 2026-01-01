import cv2
import os
import sys
import numpy as np

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from face_recognition.register_face import register_face
from face_recognition.recognize_face import recognize_face

KNOWN_FACES_DIR = os.path.join(PROJECT_ROOT, "data", "known_faces")

camera_active = False
current_mode = None
person_name = None

img_count = 0
MAX_IMAGES = 20

frame_count = 0
FRAME_GAP = 10

to_register = False

def generate_frames():
    global img_count, frame_count

    cap = cv2.VideoCapture(0)

    while camera_active:
        success, frame = cap.read()
        if not success:
            break

        if current_mode == "attendance":
            recognize_face(frame)
        elif current_mode == "registration":
            frame_count += 1
            if img_count < MAX_IMAGES and frame_count % FRAME_GAP == 0:
                to_register = True
                img_count += 1
                register_face(frame, person_name, to_register, img_count, MAX_IMAGES)
            else:
                to_register = False
                register_face(frame, person_name, to_register, img_count, MAX_IMAGES)

        ret, buffer = cv2.imencode(".jpg", frame)
        frame = buffer.tobytes()

        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")

    cap.release()