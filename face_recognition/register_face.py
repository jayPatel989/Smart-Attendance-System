import cv2
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from face_recognition.face_utils import detect_faces

def register_face(frame, person_name, to_register, img_count, max_images):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detect_faces(gray)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(
            frame,
            f"Saving Images: {img_count}/{max_images}",
            (40, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 0, 0),
            2
        )

        if len(faces) == 1 and  to_register:
            face_img = gray[y:y+h, x:x+w]

            save_dir = os.path.join(
                PROJECT_ROOT, "data", "known_faces", person_name
            )
            os.makedirs(save_dir, exist_ok=True)

            cv2.imwrite(
                os.path.join(save_dir, f"{img_count}.jpg"),
                face_img
            )