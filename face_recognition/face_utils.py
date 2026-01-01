import cv2
import dlib
import numpy as np
import os
import sys

# Load Haar Cascade file for face detection
CASCADE_PATH = os.path.join(
    os.path.dirname(__file__),
    "haarcascade_frontalface_default.xml"
)

face_cascade = cv2.CascadeClassifier(CASCADE_PATH)

def detect_faces(gray_image):
    """
    Detect faces in a grayscale image.
    Returns a list of rectangles (x, y, w, h)
    """
    faces = face_cascade.detectMultiScale(
        gray_image,
        scaleFactor=1.3,
        minNeighbors=5
    )
    return faces


# Load Dlib face recognition model
MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "dlib_face_recognition_resnet_model_v1.dat"
)

PREDICTOR_PATH = os.path.join(
    os.path.dirname(__file__),
    "shape_predictor_68_face_landmarks.dat"
)

face_recognizer = dlib.face_recognition_model_v1(MODEL_PATH)
shape_predictor = dlib.shape_predictor(PREDICTOR_PATH)


def get_face_encoding(color_image, gray_image, face_rect):
    x, y, w, h = face_rect
    rect = dlib.rectangle(x, y, x + w, y + h)

    landmarks = shape_predictor(gray_image, rect)
    rgb_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB)
    encoding = face_recognizer.compute_face_descriptor(rgb_image, landmarks)

    return np.array(encoding)


PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)
KNOWN_FACES_DIR = os.path.join(PROJECT_ROOT, "data", "known_faces")

def load_known_faces():
    known_encodings = []
    known_names = []

    for person_name in os.listdir(KNOWN_FACES_DIR):
        person_dir = os.path.join(KNOWN_FACES_DIR, person_name)

        if not os.path.isdir(person_dir):
            continue

        for img_name in os.listdir(person_dir):
            img_path = os.path.join(person_dir, img_name)

            image = cv2.imread(img_path)
            if image is None:
                continue

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            h, w = gray.shape

            fake_face_rect = (0, 0, w, h)

            encoding = get_face_encoding( image, gray, fake_face_rect)

            known_encodings.append(encoding)
            known_names.append(person_name)

    return np.array(known_encodings), known_names