import os
import pyperclip
import time
from tqdm import tqdm

Sleep = 1
trida = "faces"
trida_f = trida + ".png"
where = trida + "/"

Files = os.listdir(where)
Names = []
Out = ""
loop = 0
Out = Out + "total_faces = {}".format(len(Files)) + "\n" + "act_face = 0" + "\n"

for File in tqdm(Files) :
    loop = loop + 1
    # print(len(File))
    # if trida_f in File:
    if len(File) < 11:
        # print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        continue
    if "X" in File:
        # print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        continue
    Path = where + File
    # print(Path)
    Name = File[:-1]
    Name = Name[:-1]
    Name = Name[:-1]
    Name = Name[:-1]
    Names.append(Name)

    Full = '{} = img("{}")'.format(Name, Path)

    Out = Out + "\n" + Full
# pyperclip.copy(Out)
# time.sleep(Sleep)
# print(Out)
# print()
# print()



known_fn = "known_face_names = {}".format(Names)

known_fe = "known_face_encodings = {}".format(Names)
known_fe = known_fe.replace("'", "")

# pyperclip.copy(known_fe)
# time.sleep(Sleep)
# print(known_fe)
# print()
# print()
# pyperclip.copy(known_fn)
# time.sleep(Sleep)
# print(known_fn)

final = Out + "\n" + known_fe + "\n" + known_fn
# print(final)
pyperclip.copy(final)

# print(loop - 1)
