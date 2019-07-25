
import numpy as np
import cv2
from matplotlib import pyplot as plt

image = cv2.imread('img_MiBaRui3.jpg')
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
body = body_cascade.detectMultiScale(grayImage, 1.01, 10)

for (x,y,w,h) in body:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),3)

plt.figure(figsize=(12,12))
plt.imshow(image, cmap='gray')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

