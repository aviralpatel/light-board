import cv2
import numpy as np
from utility import compressor, lessFrame, brightestSubsetMatrix

state = True
stream = cv2.VideoCapture(1) #use 0 for default webcam
while True:
    ret, frame = stream.read()
    if state and ret:
        cv2.waitKey(10)
        state = not state
    monoColorFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #convert to greyscale
    monoColorFrame = cv2.flip(monoColorFrame, 1) #flip the captured frame
    compressedFrame = lessFrame(monoColorFrame, 5) #compress the frame and reduce the resolution by 25 for faster processing
    co_ordinates = brightestSubsetMatrix(compressedFrame, 10) #get co-ordinates
    cv2.imshow("monoclorImg", compressedFrame)
    if len(co_ordinates) > 2:
        print(f"x = {co_ordinates[1]*5} , y = {co_ordinates[0]*5}") #print the co-ordinates
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

stream.release()
cv2.destroyAllWindows()
