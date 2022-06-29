# stolen from 
import os
import face_recognition
from PIL import Image, ImageDraw
import cv2
import os

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
#  Create arrays of encodings and names

act_face = 0
total_faces = 29



IB6BrodaJakub = img("faces/IB6BrodaJakub.png")
IB6CventanovaKaterina = img("faces/IB6CventanovaKaterina.png")
IB6FisaraDavid = img("faces/IB6FisaraDavid.png")
IB6KonecnaLucie = img("faces/IB6KonecnaLucie.png")
IB6KonecnyVit = img("faces/IB6KonecnyVit.png")
IB6KriegovaPavlina = img("faces/IB6KriegovaPavlina.png")
IB6KrizAntonin = img("faces/IB6KrizAntonin.png")
IB6KubelkaErik = img("faces/IB6KubelkaErik.png")
IB6LejskovaAdela = img("faces/IB6LejskovaAdela.png")
IB6LosikovaLada = img("faces/IB6LosikovaLada.png")
IB6MacickovaJana = img("faces/IB6MacickovaJana.png")
IB6MiksikovaNatalie = img("faces/IB6MiksikovaNatalie.png")
IB6MikulovaBerenika = img("faces/IB6MikulovaBerenika.png")
IB6NajerMarek = img("faces/IB6NajerMarek.png")
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
known_face_encodings = [IB6BrodaJakub, IB6CventanovaKaterina, IB6FisaraDavid, IB6KonecnaLucie, IB6KonecnyVit, IB6KriegovaPavlina, IB6KrizAntonin, IB6KubelkaErik, IB6LejskovaAdela, IB6LosikovaLada, IB6MacickovaJana, IB6MiksikovaNatalie, IB6MikulovaBerenika, IB6NajerMarek, IB6NepovimovaLucie, IB6NovotnyOndrej, IB6PribylVojtech, IB6RobertsonTomas, IB6RybaFrantisek, IB6SedajovaSarka, IB6SobekTomas, IB6SohnelDavid, IB6StefanovaEma, IB6StrnadelMichael, IB6SyrovatkovaEliska, IB6UrbamkovaAnezka, IB6UtikalovaLLeontyna, IB6VohankovaKlara, IB6ZborilovaSara]
known_face_names = ['IB6BrodaJakub', 'IB6CventanovaKaterina', 'IB6FisaraDavid', 'IB6KonecnaLucie', 'IB6KonecnyVit', 'IB6KriegovaPavlina', 'IB6KrizAntonin', 'IB6KubelkaErik', 'IB6LejskovaAdela', 'IB6LosikovaLada', 'IB6MacickovaJana', 'IB6MiksikovaNatalie', 'IB6MikulovaBerenika', 'IB6NajerMarek', 'IB6NepovimovaLucie', 'IB6NovotnyOndrej', 'IB6PribylVojtech', 'IB6RobertsonTomas', 'IB6RybaFrantisek', 'IB6SedajovaSarka', 'IB6SobekTomas', 'IB6SohnelDavid', 'IB6StefanovaEma', 'IB6StrnadelMichael', 'IB6SyrovatkovaEliska', 'IB6UrbamkovaAnezka', 'IB6UtikalovaLLeontyna', 'IB6VohankovaKlara', 'IB6ZborilovaSara']



# what = "1.png"
def findone(where):
  # Load test image to find faces in
  test_image = face_recognition.load_image_file("wunknown/{}".format(what))

  # Find faces in test image
  face_locations = face_recognition.face_locations(test_image)
  face_encodings = face_recognition.face_encodings(test_image, face_locations)

  # Convert to PIL format
  pil_image = Image.fromarray(test_image)

  # Create a ImageDraw instance
  draw = ImageDraw.Draw(pil_image)

  # Loop through faces in test image
  for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    name = "Unknown Person"

    # If match
    if True in matches:
      first_match_index = matches.index(True)
      name = known_face_names[first_match_index]
    print(name)
    
    temp = cv2.imread("wunknown/{}".format(what))
    cv2.imwrite("wunknown/write/{}.png".format(name), temp)
    # Draw box
  #   draw.rectangle(((left, top), (right, bottom)), outline=(255,255,0))

  #   # Draw label
  #   text_width, text_height = draw.textsize(name)
  #   draw.rectangle(((left,bottom - text_height - 10), (right, bottom)), fill=(255,255,0), outline=(255,255,0))
  #   draw.text((left + 6, bottom - text_height - 5), name, fill=(0,0,0))

  # del draw

  # # Display image
  # pil_image.show()

  # # Save image
  # pil_image.save('identify.jpg')
findone("")

os.os