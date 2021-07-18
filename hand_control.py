import cv2
import mediapipe as mp
import time
import sys
import serial
#arduino = serial.Serial(port='COM3', baudrate=9600, timeout=0.01)

current_time = 0
previous_time = 0

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

# mpDraw = mp.solutions.drawing_utils




# creating named window
win_name = "Image Preview"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

def position():
    landmarkList = []
    if results.multi_hand_landmarks:
        hand_spec = results.multi_hand_landmarks[0]       
        for id, landmark in enumerate(hand_spec.landmark):
            h, w, c = frame.shape
            cx, cy = int(landmark.x*w), int(landmark.y*h)
            landmarkList.append([id, cx, cy])
    
    return landmarkList

# run till escape is pressed
while cv2.waitKey(1) != 27:
    has_frame, frame = source.read()
    if not has_frame:
        break
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    landmarks = position()
    if len(landmarks)!=0:
        control = []
        for tips in [8, 12, 16, 20]:
            if landmarks[tips][2] > landmarks[tips-2][2]:
                control.append(1)
            else:
                control.append(0)
        
        string2serial = ' '.join(map(str, control))
        string2serial = ''.join(string2serial.split())
        print(string2serial)
        #arduino.write(string2serial.encode())
        #time.sleep(3)

    # calculating fps
    current_time = time.time()
    fps = 1/(current_time - previous_time)
    previous_time = current_time
    cv2.putText(frame, str(int(fps)), (10,70), cv2.FONT_HERSHEY_COMPLEX, 3, (255,0,255), 3)


    cv2.imshow(win_name, frame)





# releasing resources
source.release
cv2.destroyWindow(win_name)



