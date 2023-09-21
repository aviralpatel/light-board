import cv2
import matplotlib.pyplot as plt
from utility import compressor, lessFrame, brightestSubsetMatrix

stream = cv2.VideoCapture(1) #use 0 for default webcam

xData = []
yData = []
fig, axes = plt.subplots()

line, = axes.plot(xData, yData)
axes.set_xlim(0, 1920)
axes.set_ylim(-1080, 0)
plt.show(block=False)


while True:
    ret, frame = stream.read()

    monoColorFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # convert to greyscale
    monoColorFrame = cv2.flip(monoColorFrame, 1)  # flip the captured frame

    compressedFrame = lessFrame(monoColorFrame, 5)  # compress the frame and reduce the resolution by 25 for faster processing

    co_ordinates = brightestSubsetMatrix(compressedFrame, 10) # get co-ordinates

    cv2.imshow("compressedFrame", compressedFrame)

    if len(co_ordinates) > 2:
        print(f"x = {co_ordinates[1]*5} , y = {co_ordinates[0]*5}")  # print the co-ordinates
        # put further code inside this if statement
        xData.append(co_ordinates[1]*5)
        yData.append(co_ordinates[0]*(-5))
        if len(xData) > 100:
            xData = xData[len(xData) - 100 : len(xData)]
            yData = yData[len(yData) - 100 : len(yData)]
        line.set_xdata(xData)
        line.set_ydata(yData)
        fig.canvas.draw()
        fig.canvas.flush_events()
        plt.pause(0.01)

    if cv2.waitKey(10) & 0xFF == ord("q"):  # waiqt 10ms for keypress
        break

stream.release()
cv2.destroyAllWindows()
