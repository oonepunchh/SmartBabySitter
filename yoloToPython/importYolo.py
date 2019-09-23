 #coding=utf-8
import os, sys, time
import signal
import subprocess
import cv2
import numpy as np

#욜로 실행할 때, 명령어 맨뒤에 이미지 파일명만 바꾸면 됨
os.chdir("C:/Users/admin/Desktop/HSEC/darknet-master/darknet-master/build/darknet/x64")
command = "darknet.exe detector demo data/coco.data cfg/yolov3.cfg yolov3.weights -c 0"
subprocess.call(command)

