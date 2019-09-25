# coding=utf-8
import os, sys, time
import signal
import subprocess
import cv2
import numpy as np

# 이거는 breathing_chest에 들어갈 파일임

cnt = 0
def extractEdge():
    global breathing_chest
    global cnt
    try:
        up = cv2.imread("C:/Users/Admin/Desktop/HSEC/darknet-master/build/darknet/x64/results/no1.jpg")
        down = cv2.imread("C:/Users/Admin/Desktop/HSEC/darknet-master/build/darknet/x64/results/no2.jpg")
        gray1 = cv2.cvtColor(up, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(down, cv2.COLOR_BGR2GRAY)

    except Exception as e:
        print(str(e))

    count = 0

    edge1 = cv2.Canny(gray1, 150, 200)
    edge2 = cv2.Canny(gray2, 150, 200)

    diff_frame = np.subtract(edge2,edge1)

    for i in range(int(len(diff_frame))):
        for j in range(int(len(diff_frame[0]))):
            if abs((int(diff_frame[i][j]))) > 250 :
                diff_frame[i][j] = 255
                count += 1
            else :
                diff_frame[i][j] = 0


    if count < 1000:
        cnt += 1
    else:
        cnt = 0
    if cnt < 10:
        breathing_chest = "True"
    else:
        breathing_chest = "False"


    return breathing_chest
