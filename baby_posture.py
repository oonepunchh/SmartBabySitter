import cv2

def faceDetect() :

    face_cascade = cv2.CascadeClassifier("C:/Users/User/PycharmProjects/edge/venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
    eye_cascade = cv2.CascadeClassifier("C:/Users/User/PycharmProjects/edge/venv/Lib/site-packages/cv2/data/haarcascade_eye.xml")

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
        eyes = eye_cascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5
        )

        #인식된 얼굴과 눈의 갯수 출력
        print("얼굴 갯수 : ",len(faces))
        print("눈 갯수 : ",len(eyes))

        #인식된 얼굴에 사각형 출력
        for (x,y,w,h) in faces :
            cv2.rectangle(frame, (x,y),(x+y,y+h),(255,0,0),2)

        #인식된 눈에 사각형 출력
        for (x,y,w,h) in eyes :
            cv2.rectangle(frame, (x,y),(x+y,y+h),(255,0,0),2)

        #화면에 출력
        cv2.imshow('posture',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
faceDetect()