import cv2

def faceDetect() :

    face_cascade = cv2.CascadeClassifier("C:/Users/User/PycharmProjects/edge/venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
    eye_cascade = cv2.CascadeClassifier("C:/Users/User/PycharmProjects/edge/venv/Lib/site-packages/cv2/data/haarcascade_eye.xml")
    left = cv2.CascadeClassifier("C:/Users/User/Anaconda3/Lib/site-packages/cv2/data/haarcascade_lefteye_2splits.xml")
    right = cv2.CascadeClassifier("C:/Users/User/Anaconda3/Lib/site-packages/cv2/data/haarcascade_righteye_2splits.xml")

    count = 0

    try :
        cam = cv2.VideoCapture(0)
        cam.set(3, 300)  # WIDTH
        cam.set(4, 400)  # HEIGHT
    except :
        print("camera loading error")
        return

    while True :
        #frame별로 캡쳐
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5
        )

        # 인식된 얼굴에 사각형 출력
        for (x, y, w, h) in faces:
            cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 255, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = gray[y:y + h, x:x + w]
            #eyes = eye_cascade.detectMultiScale(roi_gray)
            left_eye = left.detectMultiScale(roi_gray)
            right_eye = right.detectMultiScale(roi_gray)

            print("< frame %d >" % count)
            print("얼굴 갯수 : ", len(faces))
            #for (ex, ey, ew, eh) in eyes:
            #    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 127, 255), 2)
            for (ex, ey, ew, eh) in left_eye:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 127, 255), 2)
            for (ex, ey, ew, eh) in right_eye:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 127, 255), 2)
            print("왼쪽 눈 : ", len(left_eye))
            print("오른쪽 눈 : ", len(left_eye))
            #print("눈 : ",len(eyes))
            count += 1

        #화면에 출력
        cv2.imshow('posture',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
cv2.destroyAllWindows()
faceDetect()