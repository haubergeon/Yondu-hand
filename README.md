# Yondu-hand

## Setup
1. pip install opencv-python
2. pip install mediapipe
3. pip install pyserial

## The Robotic Hand
*Disclaimer - The purpose of this project was NOT to make a robotic hand but to achieve actuation in different ways.*

I've used an Arduino board, 4 servos (the fifth one broke), each to control one finger.

<img src="https://github.com/haubergeon/Yondu-hand/blob/main/images/hand1.jpg" width="100"> <img src="https://github.com/haubergeon/Yondu-hand/blob/main/images/hand2.jpg" width="100">

## Control using computer vision
I've used opencv and mediapipe to detect and track the hand and determine which finger is closed and which is open. I've then sent the data to serial port on the ardiuno using pyserial.







