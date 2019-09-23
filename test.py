import cv2
import numpy as np
import time

def pixel():

    image = cv2.imread("C:/Users/admin/Desktop/frame0.png")
    image2 = cv2.imread("C:/Users/admin/Desktopframe1.png")

    count = 0
    arr2 = [255, 255, 255]
    arr1 = [0, 0, 0]

    for i in range (int(len(image) / 3), int(len(image) * 2/3)):
        for j in range (int(len(image[0]) / 3), int(len(image[0]) * 2/3)):


            if image[i,j][0] < 10:
                image[i,j] = np.array(arr1)
            if image2[i,j][0] < 10:
                image2[i,j] = np.array(arr1)


            if (image[i,j][0] > 250) & (image[i,j][1] > 250) & (image[i,j][2] > 250) :
               image[i,j] = np.array(arr2)

            if (image2[i,j][0] > 250) & (image2[i,j][1] > 250) & (image2[i,j][2] > 250) :
               image2[i,j] = np.array(arr2)

            if str(image[i,j]) != str(image2[i,j]):
                print("다름")
                count+=1
                #print(str(image[i,j]) + " & " + str(image2[i,j]))
    print(count)
pixel()
cv2.destroyAllWindows()

