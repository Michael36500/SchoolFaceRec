import face_recognition
from PIL import Image, ImageDraw

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
act_face = 0



total_faces = 29

IB6BrodaJakub = img("known/IB6BrodaJakub.png")
IB6CventanovaKaterina = img("known/IB6CventanovaKaterina.png")
IB6FisaraDavid = img("known/IB6FisaraDavid.png")
IB6KonecnaLucie = img("known/IB6KonecnaLucie.png")
IB6KonecnyVit = img("known/IB6KonecnyVit.png")
IB6KriegovaPavlina = img("known/IB6KriegovaPavlina.png")
IB6KrizAntonin = img("known/IB6KrizAntonin.png")
IB6KubelkaErik = img("known/IB6KubelkaErik.png")
IB6LosikovaLada = img("known/IB6LosikovaLada.png")
IB6MacickovaJana = img("known/IB6MacickovaJana.png")
IB6MiksikovaNatalie = img("known/IB6MiksikovaNatalie.png")
IB6MikulovaBerenika = img("known/IB6MikulovaBerenika.png")
IB6NepovimovaLucie = img("known/IB6NepovimovaLucie.png")
IB6NovotnyOndrej = img("known/IB6NovotnyOndrej.png")
IB6PribylVojtech = img("known/IB6PribylVojtech.png")
IB6RobertsonTomas = img("known/IB6RobertsonTomas.png")
IB6RybaFrantisek = img("known/IB6RybaFrantisek.png")
IB6SedajovaSarka = img("known/IB6SedajovaSarka.png")
IB6SobekTomas = img("known/IB6SobekTomas.png")
IB6SohnelDavid = img("known/IB6SohnelDavid.png")
IB6StefanovaEma = img("known/IB6StefanovaEma.png")
IB6StrnadelMichael = img("known/IB6StrnadelMichael.png")
IB6SyrovatkovaEliska = img("known/IB6SyrovatkovaEliska.png")
IB6UrbamkovaAnezka = img("known/IB6UrbamkovaAnezka.png")
IB6UtikalovaLLeontyna = img("known/IB6UtikalovaLLeontyna.png")
IB6VohankovaKlara = img("known/IB6VohankovaKlara.png")
IB6ZborilovaSara = img("known/IB6ZborilovaSara.png")
known_face_encodings = [IB6BrodaJakub, IB6CventanovaKaterina, IB6FisaraDavid, IB6KonecnaLucie, IB6KonecnyVit, IB6KriegovaPavlina, IB6KrizAntonin, IB6KubelkaErik, IB6LosikovaLada, IB6MacickovaJana, IB6MiksikovaNatalie, IB6MikulovaBerenika, IB6NepovimovaLucie, IB6NovotnyOndrej, IB6PribylVojtech, IB6RobertsonTomas, IB6RybaFrantisek, IB6SedajovaSarka, IB6SobekTomas, IB6SohnelDavid, IB6StefanovaEma, IB6StrnadelMichael, IB6SyrovatkovaEliska, IB6UrbamkovaAnezka, IB6UtikalovaLLeontyna, IB6VohankovaKlara, IB6ZborilovaSara]
known_face_names = ['IB6BrodaJakub', 'IB6CventanovaKaterina', 'IB6FisaraDavid', 'IB6KonecnaLucie', 'IB6KonecnyVit', 'IB6KriegovaPavlina', 'IB6KrizAntonin', 'IB6KubelkaErik', 'IB6LosikovaLada', 'IB6MacickovaJana', 'IB6MiksikovaNatalie', 'IB6MikulovaBerenika', 'IB6NepovimovaLucie', 'IB6NovotnyOndrej', 'IB6PribylVojtech', 'IB6RobertsonTomas', 'IB6RybaFrantisek', 'IB6SedajovaSarka', 'IB6SobekTomas', 'IB6SohnelDavid', 'IB6StefanovaEma', 'IB6StrnadelMichael', 'IB6SyrovatkovaEliska', 'IB6UrbamkovaAnezka', 'IB6UtikalovaLLeontyna', 'IB6VohankovaKlara', 'IB6ZborilovaSara']


# Load test image to find faces in
test_image = face_recognition.load_image_file('unknown/1.png')

# Find faces in test image
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

# Convert to PIL format
pil_image = Image.fromarray(test_image)

# Create a ImageDraw instance
draw = ImageDraw.Draw(pil_image)

# Loop through faces in test image
for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.face_distance(known_face_encodings, face_encoding)

    name = "Unknown Person"

    # If match
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    # Draw box
    draw.rectangle(((left, top), (right, bottom)), outline=(255,255,0))

    # Draw label
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left,bottom - text_height - 10), (right, bottom)), fill=(255,255,0), outline=(255,255,0))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(0,0,0))

del draw

# Display image
pil_image.show()

# Save image
pil_image.save('identify.jpg')