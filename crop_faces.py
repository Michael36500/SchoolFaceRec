import cv2
import numpy

full = cv2.imread("rocenka.png")
cv2.imshow('Original Image', full)
cv2.waitKey()
crop = []


crop = full[50:180, 100:300]  