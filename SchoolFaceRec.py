import face_recognition
import cv2
from imageio import volread
import numpy as np
# import def_load as load
import random as rn
import time

Start = time.time()

import face_recognition
import cv2
import numpy as np
from scipy.misc import face
act_face = 0

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

def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
print("GO!")

# Load a sample picture and learn how to recognize it.
total_faces = 1023
camera = 1
video_capture = cv2.VideoCapture(camera, cv2.CAP_DSHOW)
time.sleep(1)
video_capture.release()



total_faces = 1036
act_face = 0

AbrahamovaTv = img("faces/AbrahamovaTv.jpg")
Adamikova2AjRuD = img("faces/Adamikova2AjRuD.jpg")
BednarikovaMaITV = img("faces/BednarikovaMaITV.jpg")
BerankovaAjFr = img("faces/BerankovaAjFr.jpg")
BraunerChBi = img("faces/BraunerChBi.jpg")
CastellarSp = img("faces/CastellarSp.jpg")
CechovaAj = img("faces/CechovaAj.jpg")
ChromaTvZ = img("faces/ChromaTvZ.jpg")
DanielTvZ = img("faces/DanielTvZ.jpg")
DohnalovaCjHv = img("faces/DohnalovaCjHv.jpg")
DostalovaTv = img("faces/DostalovaTv.jpg")
known_face_encodings = [AbrahamovaTv, Adamikova2AjRuD, BednarikovaMaITV, BerankovaAjFr, BraunerChBi, CastellarSp, CechovaAj, ChromaTvZ, DanielTvZ, DohnalovaCjHv, DostalovaTv]
known_face_names = ['AbrahamovaTv', 'Adamikova2AjRuD', 'BednarikovaMaITV', 'BerankovaAjFr', 'BraunerChBi', 'CastellarSp', 'CechovaAj', 'ChromaTvZ', 'DanielTvZ', 'DohnalovaCjHv', 'DostalovaTv']









print("pictures loaded")
print(time.time() - Start)

# for a in range(10):
#     print("trying", a)
#     video_capture = cv2.VideoCapture(a, cv2.CAP_DSHOW)
#     reat, frame = video_capture.read()
#     print(ret)
#     if ret == True:
#         break
#     else:
#         video_capture.release()
video_capture = cv2.VideoCapture(camera, cv2.CAP_DSHOW)
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
# video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)




print("video captured")
# print(video_capture)
# Initialize some variables
multipl = 1
resize = 1 / multipl
face_locations = [] 
face_encodings = []
face_names = []
process_this_frame = True
print("variables")
loop_noob = 0
while True:
    loop_noob = loop_noob + 1
    # Grab a single frame of video
    ret, frame = video_capture.read()
    if "None" in str(frame):
        print("dont have frame, skiping it")
        continue
    frame = cv2.resize(frame, (960, 540))
    print(ret, loop_noob)

    # Resize frame of video to 1/4 size for faster face recognition processing
    # small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    small_frame = cv2.resize(frame, (0, 0), fx=resize, fy=resize)
    # small_frame = frame

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        print("debuging is fun")
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

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

    process_this_frame = not process_this_frame


    # Display the results
    # print("tum")
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        # top *= 4
        # right *= 4
        # bottom *= 4
        # left *= 4
        top *= multipl
        right *= multipl
        bottom *= multipl
        left *= multipl

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (255, 0, 0), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255 ), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)
    time.sleep(0.1)

    # # Hit 'q' on the keyboard to quit!
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     # print("there")
    #     break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
 