import cv2
import numpy as np
import time

def pixel():
    start = time.time()
    image = cv2.imread("/mnt/c/Users/Admin/Desktop/python/frame0.jpg")
    image2 = cv2.imread("/mnt/c/Users/Admin/Desktop/python/frame80.jpg")

    gray1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    diff_frame = gray2 - gray1
    diff_frame -= diff_frame.min()
    disp_frame = np.uint8(255.0*diff_frame/float(diff_frame.max()))

    print(disp_frame)
    print("--")
    count = 0
    for i in range (int(len(disp_frame))) :
        for j in range (int(len(disp_frame[0]))) :
            if (int(disp_frame[i][j])) == 255 :
                count+=1
    print(count)
    print(time.time() - start)
    print(cv2.__version__)
pixel()
cv2.destroyAllWindows()

