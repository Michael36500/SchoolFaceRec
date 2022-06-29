import face_recognition
import cv2
from imageio import volread
import numpy as np
import random as rn
import time
from scipy.misc import face
import os
from tqdm import tqdm

files = os.listdir("test/")
print(files)


act_face = 0
total_faces = 30

def img(where):
    global total_faces
    global act_face
    act_face = act_face + 1
    print("picture loaded ", where, "\t\t\t\t", act_face, "of", total_faces)
    image = face_recognition.load_image_file(where)
    # print(image)
    
    face_encoding = face_recognition.face_encodings(image)
    if str(face_encoding) == "[]":
        print("NO FINDABLE FACES!!!")
    # face_encoding = face_encoding[0]
    # print(face_encoding)

    return face_encoding [0]
total_faces = 5




IB6StrnadelMichael = img("faces/IB6StrnadelMichael.png")
IB6UrbamkovaAnezka = img("faces/IB6UrbamkovaAnezka.png")
IB6UtikalovaLLeontyna = img("faces/IB6UtikalovaLLeontyna.png")
IB6VohankovaKlara = img("faces/IB6VohankovaKlara.png")
IB6ZborilovaSara = img("faces/IB6ZborilovaSara.png")
known_face_encodings = [IB6StrnadelMichael, IB6UrbamkovaAnezka, IB6UtikalovaLLeontyna, IB6VohankovaKlara, IB6ZborilovaSara]
known_face_names = ['IB6StrnadelMichael', 'IB6UrbamkovaAnezka', 'IB6UtikalovaLLeontyna', 'IB6VohankovaKlara', 'IB6ZborilovaSara']


for file in tqdm(files):
    img = cv2.imread("test/{}".format(file))
    face_locations = face_recognition.face_locations(img)
    face_encoding = face_recognition.face_encodings(img)    

    results = face_recognition.compare_faces(known_face_encodings, face_encoding)
    print(results)