import cv2

def faceDetect():

    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    left_eye_detector = cv2.CascadeClassifier("haarcascade_lefteye_2splits.xml")
    right_eye_detector = cv2.CascadeClassifier("haarcascade_righteye_2splits.xml")

    count = 0

    try:
        cam = cv2.VideoCapture(0)
        cam.set(3, 300)  # WIDTH
        cam.set(4, 400)  # HEIGHT
    except:
        print("camera loading error")
        return

    while cam.read(True):
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5
        )

        for (x, y, w, h) in faces:
            #left_face = frame[y:y + h, x + int(w / 2):x + w]
            left_face_gray = gray[y:y + h, x + int(w / 2):x + w]

            #right_face = frame[y:y + h, x:x + int(w / 2)]
            right_face_gray = gray[y:y + h, x:x + int(w / 2)]

            # Detect the left eye
            left_eye = left_eye_detector.detectMultiScale(
                left_face_gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )

            # Detect the right eye
            right_eye = right_eye_detector.detectMultiScale(
                right_face_gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )

            cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 255, 0), 2)
            #roi_gray = gray[y:y + h, x:x + w]
            roi_color = gray[y:y + h, x:x + w]

            print("< frame %d >" % count)

            for (ex, ey, ew, eh) in left_eye:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 127, 255), 2)
            for (ex, ey, ew, eh) in right_eye:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 127, 255), 2)

            count += 1

        if (len(left_eye) == 0 | len(right_eye) == 0):
            print("고개 돌아감")
        elif (len(left_eye) == 1 & len(right_eye) == 1):
            print("고개 정면")
        else:
            print("고개 돌아감")

        cv2.imshow('posture',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
cv2.destroyAllWindows()
faceDetect()