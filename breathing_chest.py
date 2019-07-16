import cv2

def showVideo() :
    try :
        print('camera working')
        vidcap = cv2.VideoCapture(0) #비디오 재생 + 캡처
    except :
        print('camera loading error')
        return

    count = 0 # frame수 넣어주기 위한 변수

    while vidcap.isOpened() :
        #라이브 비디오 프레임 별 캡쳐 -> 디스플레이
        #cap.read = 비디오 한 프레임씩 읽어서
        #비디오 프레임 제대로 읽히면 ret = True / 실패시 ret = False
        ret, frame = vidcap.read()

        if not ret :
            print('video read error')
            break

        # frame을 흑백 영상으로 변환
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Canny 에지 검출기 (Edge검출)
        canny = cv2.Canny(gray,50,200)

        # 캡쳐된 이미지 저장
        cv2.imwrite("C:/Users/User/Desktop/python/frame%d.jpg" % count, canny)
        print('Saved frame %d.jpg' % count)
        count += 1

        cv2.imshow('video',gray)

        k = cv2.waitKey(1) & 0xFF
        if k == 27 : # 여기서 27이 뭔지를 모르겠는데 아마 q or esc키 일듯함.. i dont know..
            break
    vidcap.release() #오픈한 vidcap객체에 대한 해제
    vidcap.destroyAllWindows() #모든 윈도우 제거

showVideo()