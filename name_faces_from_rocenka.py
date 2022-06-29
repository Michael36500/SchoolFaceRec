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
    
    face_encoding = face_recognition.face_encodings(image)[0]
    if str(face_encoding) == "[]":
        print("NO FINDABLE FACES!!!")
    # face_encoding = face_encoding[0]
    # print(face_encoding)

    return face_encoding [0]

total_faces = 30




IB6BrodaJakub = img("faces/IB6BrodaJakub.png")
IB6CventanovaKaterina = img("faces/IB6CventanovaKaterina.png")
IB6FisaraDavid = img("faces/IB6FisaraDavid.png")
IB6KonecnaLucie = img("faces/IB6KonecnaLucie.png")
IB6KonecnyVit = img("faces/IB6KonecnyVit.png")
IB6KriegovaPavlina = img("faces/IB6KriegovaPavlina.png")
IB6KrizAntonin = img("faces/IB6KrizAntonin.png")
IB6KubelkaErik = img("faces/IB6KubelkaErik.png")
IB6LosikovaLada = img("faces/IB6LosikovaLada.png")
IB6MacickovaJana = img("faces/IB6MacickovaJana.png")
IB6MiksikovaNatalie = img("faces/IB6MiksikovaNatalie.png")
IB6MikulovaBerenika = img("faces/IB6MikulovaBerenika.png")
IB6NepovimovaLucie = img("faces/IB6NepovimovaLucie.png")
IB6NovotnyOndrej = img("faces/IB6NovotnyOndrej.png")
IB6PribylVojtech = img("faces/IB6PribylVojtech.png")
IB6RobertsonTomas = img("faces/IB6RobertsonTomas.png")
IB6RybaFrantisek = img("faces/IB6RybaFrantisek.png")
IB6SedajovaSarka = img("faces/IB6SedajovaSarka.png")
IB6SobekTomas = img("faces/IB6SobekTomas.png")
IB6SohnelDavid = img("faces/IB6SohnelDavid.png")
IB6StefanovaEma = img("faces/IB6StefanovaEma.png")
IB6StrnadelMichael = img("faces/IB6StrnadelMichael.png")
IB6SyrovatkovaEliska = img("faces/IB6SyrovatkovaEliska.png")
IB6UrbamkovaAnezka = img("faces/IB6UrbamkovaAnezka.png")
IB6UtikalovaLLeontyna = img("faces/IB6UtikalovaLLeontyna.png")
IB6VohankovaKlara = img("faces/IB6VohankovaKlara.png")
IB6ZborilovaSara = img("faces/IB6ZborilovaSara.png")
known_face_encodings = [IB6BrodaJakub, IB6CventanovaKaterina, IB6FisaraDavid, IB6KonecnaLucie, IB6KonecnyVit, IB6KriegovaPavlina, IB6KrizAntonin, IB6KubelkaErik, IB6LosikovaLada, IB6MacickovaJana, IB6MiksikovaNatalie, IB6MikulovaBerenika, IB6NepovimovaLucie, IB6NovotnyOndrej, IB6PribylVojtech, IB6RobertsonTomas, IB6RybaFrantisek, IB6SedajovaSarka, IB6SobekTomas, IB6SohnelDavid, IB6StefanovaEma, IB6StrnadelMichael, IB6SyrovatkovaEliska, IB6UrbamkovaAnezka, IB6UtikalovaLLeontyna, IB6VohankovaKlara, IB6ZborilovaSara]
known_face_names = ['IB6BrodaJakub', 'IB6CventanovaKaterina', 'IB6FisaraDavid', 'IB6KonecnaLucie', 'IB6KonecnyVit', 'IB6KriegovaPavlina', 'IB6KrizAntonin', 'IB6KubelkaErik', 'IB6LosikovaLada', 'IB6MacickovaJana', 'IB6MiksikovaNatalie', 'IB6MikulovaBerenika', 'IB6NepovimovaLucie', 'IB6NovotnyOndrej', 'IB6PribylVojtech', 'IB6RobertsonTomas', 'IB6RybaFrantisek', 'IB6SedajovaSarka', 'IB6SobekTomas', 'IB6SohnelDavid', 'IB6StefanovaEma', 'IB6StrnadelMichael', 'IB6SyrovatkovaEliska', 'IB6UrbamkovaAnezka', 'IB6UtikalovaLLeontyna', 'IB6VohankovaKlara', 'IB6ZborilovaSara']



for file in tqdm(files):
    img = cv2.imread("test/{}".format(file))
    unface_locations = face_recognition.face_locations(img)
    unface_encoding = face_recognition.face_encodings(img) [0]


    results = face_recognition.compare_faces([known_face_encodings], unface_encoding)
    cv2.imsave("test/{}.png".format())
    print(results)
    