import face_recognition
import cv2
from matplotlib import mathtext
import numpy as np
from scipy.misc import face
import face_recognition
import cv2
from imageio import volread
import numpy as np
# import def_load as load
import random as rn
import time



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
known_face_encodings = [[IB6BrodaJakub], [IB6CventanovaKaterina], [IB6FisaraDavid], [IB6KonecnaLucie], [IB6KonecnyVit], [IB6KriegovaPavlina], [IB6KrizAntonin], [IB6KubelkaErik], [IB6LosikovaLada], [IB6MacickovaJana], [IB6MiksikovaNatalie], [IB6MikulovaBerenika], [IB6NepovimovaLucie], [IB6NovotnyOndrej], [IB6PribylVojtech], [IB6RobertsonTomas], [IB6RybaFrantisek], [IB6SedajovaSarka], [IB6SobekTomas], [IB6SohnelDavid], [IB6StefanovaEma], [IB6StrnadelMichael], [IB6SyrovatkovaEliska], [IB6UrbamkovaAnezka], [IB6UtikalovaLLeontyna], [IB6VohankovaKlara], [IB6ZborilovaSara]]
known_face_names = ['IB6BrodaJakub', 'IB6CventanovaKaterina', 'IB6FisaraDavid', 'IB6KonecnaLucie', 'IB6KonecnyVit', 'IB6KriegovaPavlina', 'IB6KrizAntonin', 'IB6KubelkaErik', 'IB6LosikovaLada', 'IB6MacickovaJana', 'IB6MiksikovaNatalie', 'IB6MikulovaBerenika', 'IB6NepovimovaLucie', 'IB6NovotnyOndrej', 'IB6PribylVojtech', 'IB6RobertsonTomas', 'IB6RybaFrantisek', 'IB6SedajovaSarka', 'IB6SobekTomas', 'IB6SohnelDavid', 'IB6StefanovaEma', 'IB6StrnadelMichael', 'IB6SyrovatkovaEliska', 'IB6UrbamkovaAnezka', 'IB6UtikalovaLLeontyna', 'IB6VohankovaKlara', 'IB6ZborilovaSara']



image = face_recognition.load_image_file("test/1.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

face_locations = face_recognition.face_locations(image)
face_encodings = face_recognition.face_encodings(image, face_locations)

face_names = []
for face_encoding in face_encodings:
    # See if the face is a match for the known face(s)
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    name = "Unknown"

    # # If a match was found in known_face_encodings, just use the first one.
    # if True in matches:
    #     first_match_index = matches.index(True)
    #     name = known_face_names[first_match_index]

    # Or instead, use the known face with the smallest distance to the new face
    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
    best_match_index = np.argmin(face_distances)
    if matches[best_match_index]:
        name = known_face_names[best_match_index]

    face_names.append(name)
print(face_names)