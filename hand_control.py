import cv2
import mediapipe as mp
import time
import sys

current_time = 0
previous_time = 0

check = True
landmarkList = []
fingerList = []

# choosing camera
s = 0
if len(sys.argv) > 1:
    s = sys.argv[1]
source = cv2.VideoCapture(s)

# MEDIAPIPE hands
mpHand = mp.solutions.hands
hands = mpHand.Hands(static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,)

mpDraw = mp.solutions.drawing_utils




# creating named window
win_name = "Image Preview"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

# run till escape is pressed
while cv2.waitKey(1) != 27:
    has_frame, frame = source.read()
    if not has_frame:
        break
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    # prints none if no hand is in frame

    if results.multi_hand_landmarks:
        for handLandmarks in results.multi_hand_landmarks:

            # getting the location of various landmarks
            if check == True:
                
                for id, landmark in enumerate(handLandmarks.landmark):
                    # print(id, landmark)
                    h, w, c = frame.shape
                    cx, cy = int(landmark.x*w), int(landmark.y*h)

                    # print(id, cx, cy)
                    landmarkList.append([id, cx, cy])


            mpDraw.draw_landmarks(frame, handLandmarks, mpHand.HAND_CONNECTIONS)

    # calculating fps
    current_time = time.time()
    fps = 1/(current_time - previous_time)
    previous_time = current_time
    cv2.putText(frame, str(int(fps)), (10,70), cv2.FONT_HERSHEY_COMPLEX, 3, (255,0,255), 3)


    cv2.imshow(win_name, frame)





# releasing resources
source.release
cv2.destroyWindow(win_name)
