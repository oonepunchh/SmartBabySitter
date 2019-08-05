import cv2

def pixel():
    image = cv2.imread("C:/Users/Admin/Desktop/python/frame0.jpg")

    for i in range (0, len(image[0])):
        for j in range (0, len(image)):
            if str(image[i,j]) == "[255 255 255]":
                print(str(i) + " " + str(j))

pixel()
cv2.destroyAllWindows()

