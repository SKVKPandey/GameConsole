import cv2
import mediapipe as mp
import time
import pyautogui

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
pTime = 0
cTime = 0
cx = 0
cy = 0
current_key = ''

while(True):
	
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                if id == 8:
                    cv2.circle(img, (cx,cy), 10, (255, 0, 255), cv2.FILLED)

                    if cx in range(300,350) and cy in range(67,110):
                        current_key = 'enter'
                        pyautogui.keyDown(current_key)
                        
                    elif cx in range(172,215) and cy in range(215,265):
                        current_key = 'left'
                        pyautogui.keyDown(current_key)

                    elif cx in range(435,478) and cy in range(215,265):
                        current_key = 'right'
                        pyautogui.keyDown(current_key)

                    else:
                        pyautogui.keyUp(current_key)
                                      
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, "FPS: "+str(int(fps)), (18, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    l1_start_point = (300, 110)
    l1_end_point = (350,110)
    # l2_start_point = (300,370)
    # l2_end_point = (350,370)
    l3_start_point = (215,215)
    l3_end_point = (215,265)
    l4_start_point = (435,215)
    l4_end_point = (435,265)

    ta1_start_point = l1_start_point
    ta1_end_point = ((l1_start_point[0]+l1_end_point[0])//2,l1_start_point[1]-43)
    tb1_start_point = l1_end_point
    tb1_end_point = ta1_end_point

    ta3_start_point = l3_start_point
    ta3_end_point = (l3_start_point[0]-43, (l3_start_point[1]+l3_end_point[1])//2)
    tb3_start_point = l3_end_point
    tb3_end_point = ta3_end_point

    ta4_start_point = l4_start_point
    ta4_end_point = (l4_start_point[0]+43, (l4_start_point[1]+l4_end_point[1])//2)
    tb4_start_point = l4_end_point
    tb4_end_point = ta4_end_point

    cv2.line(img, l1_start_point, l1_end_point, (0,0,255), 2)

    cv2.line(img, l3_start_point, l3_end_point, (0,255,255), 2)
    cv2.line(img, l4_start_point, l4_end_point, (0,255,255), 2)

    cv2.line(img, ta1_start_point, ta1_end_point, (0,0,255), 2)
    

    cv2.line(img, ta3_start_point, ta3_end_point, (0,255,255), 2)
    cv2.line(img, ta4_start_point, ta4_end_point, (0,255,255), 2)

    cv2.line(img, tb1_start_point, tb1_end_point, (0,0,255), 2)
    

    cv2.line(img, tb3_start_point, tb3_end_point, (0,255,255), 2)
    cv2.line(img, tb4_start_point, tb4_end_point, (0,255,255), 2)

    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
	    break


cap.release()

cv2.destroyAllWindows()