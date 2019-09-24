# coding=utf-8
import os, sys, time
import signal
import subprocess
import cv2
import numpy as np
#이거는 breathing_chest에 들어갈 파일임
global breathing_chest

def extractEdge():
    try:
        up = cv2.imread("1.png")
        down = cv2.imread("2.png")
        gray1 = cv2.cvtColor(up, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(down, cv2.COLOR_BGR2GRAY)

    except Exception as e:
        print(str(e))

    count = 0

    edge1 = cv2.Canny(gray1, 80, 120)
    edge2 = cv2.Canny(gray2, 80, 120)

    # cv2.imshow('Canny Edge up compare', edge1)
    # cv2.imshow('Canny Edge down compare', edge2)

    diff_frame = edge1 - edge2

    diff_frame -= diff_frame.min()
    # disp_frame = np.uint8(255.0*diff_frame/float(diff_frame.max()))

    for i in range(int(len(diff_frame))):
        for j in range(int(len(diff_frame[0]))):
            if (int(diff_frame[i][j])) == 255:
                diff_frame[i][j] = 255
                count += 1
            elif (int(diff_frame[i][j])) < 255:
                diff_frame[i][j] = 0
    if count > 1500:
        breathing_chest = True
    else:
        breathing_chest = False

    # cv2.imshow('different', diff_frame)
    print(count)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return breathing_chest
# os.chdir("C:/Users/admin/Desktop/HSEC/darknet-master/darknet-master/build/darknet/x64")

# Print current working directory
# print ("Current working dir : %s" % os.getcwd())


# 욜로 실행할 때, 명령어 맨뒤에 이미지 파일명만 바꾸면 됨
# command = "darknet.exe detector test ./cfg/coco.data ./cfg/yolov3.cfg ./yolov3.weights baby6.jpg"
# subprocess.call(command)