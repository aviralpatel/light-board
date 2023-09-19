import cv2
import numpy as np
from utility import compressor, lessFrame

state = True
stream = cv2.VideoCapture(0)
while True:
    ret, frame = stream.read()
    if state and ret:
        cv2.imwrite("./images/frame.jpg", frame)
        state = not state
    monoColorFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    monoColorFrame = cv2.flip(monoColorFrame, 1)
    compressedFrame = lessFrame(monoColorFrame, 5)
    #print(monoColorFrame.shape)
    #compressedFrame = compressor(monoColorFrame, 5)
    print(compressedFrame)
    cv2.imshow("monoclorImg", monoColorFrame)
    cv2.imshow("CompressedImg", compressedFrame)
    #cv2.imshow("compressedStream", compressedFrame)
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

stream.release()
cv2.destroyAllWindows()