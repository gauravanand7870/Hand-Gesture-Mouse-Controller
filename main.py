import cv2
import numpy as np
import TrackingModule as htm
import time
import autopy


wCam, hCam = 640, 480
frameR = 100  # Frame Reduction
smooth = 7  #smoothening factor


pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0
#vid = cv2.VideoCapture(0)
vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)   #Using a different API for capturing video
time.sleep(0.5)


vid.set(3, wCam)
vid.set(4, hCam)
detector = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()


while True:
    #  Find hand Landmarks
    success, img = vid.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    #  Get the tip of the index and middle fingers
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        x3, y3 = lmList[16][1:]  # ring finger
        # print(x1, y1, x2, y2)


    fingers = detector.fingersUp()
    # print(fingers)
    cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
                  (255, 0, 255), 2)
    #  Only Index Finger : Moving Mode
    if fingers[1] == 1 and fingers[2] == 0:
        #  Convert Coordinates
        x_new = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
        y_new = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
        #  Smoothen Values
        clocX = plocX + (x_new - plocX) / smooth
        clocY = plocY + (y_new - plocY) / smooth

        #  Move Mouse
        autopy.mouse.move(wScr - clocX, clocY)
        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        plocX, plocY = clocX, clocY

    #  Both Index and middle fingers are up : Clicking Mode
    if fingers[1] == 1 and fingers[2] == 1:
        #  Find distance between fingers
        length, img, lineInfo = detector.findDistance(8, 12, img)
        print(length)
        #  Click mouse if distance short
        if length < 40:
            cv2.circle(img, (lineInfo[4], lineInfo[5]),
                       15, (0, 255, 0), cv2.FILLED)
            autopy.mouse.click()
    # Index, middle and ring finger up; right click
    if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1:
        length1, _, _ = detector.findDistance(8, 12, img, draw=False)
        length2, _, _ = detector.findDistance(12, 16, img, draw=False)
        length3, _, _ = detector.findDistance(12, 16, img, draw=False)
        if length1 < 40 and length2 < 40 and length3 < 40:  # all distances should be small
            autopy.mouse.click(button=autopy.mouse.Button.RIGHT)
            cv2.circle(img, (lineInfo[4], lineInfo[5]),
                       15, (0, 0, 255), cv2.FILLED)

    # 11. Frame Rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)
    # 12. Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)