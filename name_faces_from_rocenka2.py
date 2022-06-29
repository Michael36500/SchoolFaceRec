from base64 import encode
import face_recognition as fr
import cv2 as cv
import time
import os

target_image = fr.load_image_file("test/2.png")
target_encoding = fr.face_encodings(target_image)


def encode_faces(folder):
    list_people_encoding = []

    for filename in os.listdir(folder):
        known_image = fr.load_image_file("{}{}".format(folder, filename))
        known_encoding = fr.face_encodings(known_image)[0]

        list_people_encoding.append((known_encoding, filename))
        
        return list_people_encoding

def find_target_face():
    face_location = fr.face_locations(target_image)
    # for person in encode_faces("IB6DONET/"):
    for person in encode_faces("IB6DONET/"):
        encoded_face = person[0]
        filename = person[1]

        is_target_face = fr.compare_faces(encoded_face, target_encoding, tolerance=0.6)
        print(is_target_face, filename)

        if str(is_target_face) != "[False]":
            print(is_target_face)


        if face_location:
            face_number = 0
            for location in face_location:
                if is_target_face[face_number]:
                    label = filename
                    create_frame(location, label)
                face_number += 1

def create_frame(location, label):
    top, right, bot, left = location
    cv.rectangle(target_image, (left, top), (right, bot), (255, 0, 0), 2)
    print(label)

def render_image():
    rgb_img = cv.cvtColor(target_image, cv.COLOR_BGR2RGB)
    cv.imshow("face rec", rgb_img)
    # time.sleep(5)
    cv.waitKey(0)


find_target_face()
render_image()