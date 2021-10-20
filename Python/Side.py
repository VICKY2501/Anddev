import cv2
import numpy as np


def nothing(x):
    # any operation
    pass


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cv2.namedWindow("Trackbars")
cv2.createTrackbar("L-H", "Trackbars", 110, 180, nothing)
cv2.createTrackbar("L-S", "Trackbars", 90, 255, nothing)
cv2.createTrackbar("L-V", "Trackbars", 60, 255, nothing)
cv2.createTrackbar("U-H", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("U-S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U-V", "Trackbars", 243, 255, nothing)

font = cv2.FONT_HERSHEY_COMPLEX



while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)


    dst = cv2.cornerHarris(gray, 5,5,0.2)
    frame[dst > 0.01 * dst.max()] = [0, 0, 0]


    l_h = cv2.getTrackbarPos("L-H", "Trackbars")
    l_s = cv2.getTrackbarPos("L-S", "Trackbars")
    l_v = cv2.getTrackbarPos("L-V", "Trackbars")
    u_h = cv2.getTrackbarPos("U-H", "Trackbars")
    u_s = cv2.getTrackbarPos("U-S", "Trackbars")
    u_v = cv2.getTrackbarPos("U-V", "Trackbars")

    lower_red = np.array([l_h, l_s, l_v])
    upper_red = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.erode(mask, kernel)
    mask=cv2.dilate(mask, kernel)
    edge = cv2.Canny(mask, 10, 200)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    black = np.zeros([50, 50, 3])

    for cnt in contours:
        area = cv2.contourArea(cnt)
        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True),True)
        x = approx.ravel()[0]
        y = approx.ravel()[1]


        if area > 1000:
            cv2.drawContours(frame,[approx],0,(0,255,0), 3)

            arr= cv2.findContours()[a]

            for b in a:


            n = approx.ravel()
            i = 0

            for j in n:
                if (i % 2 == 0):
                    x = n[i]
                    y = n[i + 1]

                    # String containing the co-ordinates.
                    string = str(x) + " " + str(y)


                    if (i == 0):
                        # text on topmost co-ordinate.
                        cv2.putText(frame, string, (x, y), font, 0.5, (255, 0, 0))
                    else:
                        # text on remaining co-ordinates.
                        cv2.putText(frame, string, (x, y), font, 0.5, (0, 255, 0))
                i = i + 1


    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Edge",edge)



    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()