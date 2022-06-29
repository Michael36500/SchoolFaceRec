import face_recognition
import cv2
from tqdm import tqdm
import os
def crop_faces(trida):
    os.makedirs(trida, exist_ok=True)
    # trida = "IA6"
    print(trida)
    # os.makedirs(trida, exist_ok=True)
    # img = face_recognition.load_image_file("skeny/{}.png".format(trida))
    img = face_recognition.load_image_file("zskeny/{}.png".format(trida))
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_rgb_copy = img_rgb.copy()

    ## Define scale factor and window size
    scale_factor = 1.1
    sz1 = img_rgb.shape[1] * 2
    sz2 = img_rgb.shape[0] * 2
    # print("before")
    face_locations = face_recognition.face_locations(img_rgb)
    # print("after")
    lpnb = 0
    for top, right, bottom, left in tqdm(face_locations):
        lpnb = lpnb + 1
        # Draw a box around the face
        #cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)

        offset = 120

        crop_img = img_rgb[top-offset:bottom+offset, left-offset:right+offset]



        ## Calculate center points and rectangle side length
        # width = right - left
        # height = bottom - top
        # cX = left + width // 2
        # cY = top + height // 2
        # M = (abs(width) + abs(height)) / 2


        ## Get the resized rectangle points
        # newLeft = max(0, int(cX - scale_factor * M))
        # newTop = max(0, int(cY - scale_factor * M))
        # newRight = min(img_rgb.shape[1], int(cX + scale_factor * M))
        # newBottom = min(img_rgb.shape[0], int(cY + scale_factor * M))


        ## Draw the circle and bounding boxes
        # cv2.circle(img_rgb_copy, (cX, cY), radius=0, color=(0, 0, 255), thickness=2)
        # cv2.rectangle(img_rgb_copy, (left, top), (right, bottom), (0, 0, 255), 2)
        # cv2.rectangle(img_rgb_copy, (newLeft, newTop), (newRight, newBottom), (255, 0, 0), 2)


        ## Show the original image in window resized to double
        # cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        # cv2.resizeWindow('image', sz1, sz2)
        # cv2.imshow("image", crop_img)
        # cv2.waitKey(100)
        # cv2.imwrite('{}/{}.png'.format(trida, lpnb), crop_img)
        cv2.imwrite('{}/{}.png'.format(trida, lpnb), crop_img)



    # cv2.destroyAllWindows()

# inputs_jpg = os.listdir("skeny/")
# inputs = []
# for a in tqdm(inputs_jpg):
#     l = len(a)
#     short = a[:l - 4]
#     crop_faces(short)
# crop_faces("IB6")

inputs_jpg = os.listdir("skeny/")
inputs = []
for a in tqdm(inputs_jpg):
    l = len(a)
    short = a[:l - 4]
    crop_faces(short)