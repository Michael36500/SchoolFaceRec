import face_recognition
import cv2
import numpy as np
from scipy.misc import face

def img(where):
    global total_faces
    global act_face
    
    print("picture loaded    ", where,"   ", act_face)
    image = face_recognition.load_image_file(where)
    # print(image)
    
    face_encoding = face_recognition.face_encodings(image)
    if str(face_encoding) == "[]":
        print("NO FINDABLE FACES!!!")
    # face_encoding = face_encoding[0]
    # print(face_encoding)

    return face_encoding [0]