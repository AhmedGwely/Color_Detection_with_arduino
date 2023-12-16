import cv2
from PIL import Image
import controler as cnt
from color_range import get_limits

color = [0, 255, 0]   #BGR   yellow


webcam = cv2.VideoCapture(1)


fbs = int(webcam.get(cv2.CAP_PROP_FPS))
print(fbs)


while True:
    st, frame = webcam.read()

    hsv_frames = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimits, upperLimits = get_limits(color)

    mask = cv2.inRange(hsv_frames,lowerLimits,upperLimits)

    mask_ = Image.fromarray(mask)

    bondary_box = mask_.getbbox()
    print(bondary_box)
    # return table of 4 numbers that represent rectangle boundary and it is tuple

    if bondary_box:

        x1, y1, w, h = bondary_box
        box = cv2.rectangle(frame, (x1, y1), (w, h), (0, 255, 0), 4,)
    if bondary_box:
        cnt.led(1)
    else:
        cnt.led(0)
    #cnt.led(0)

    if st:

        cv2.imshow("live", frame)
        if cv2.waitKey(fbs) & 0xFF == ord('x'):
            break
        

    


webcam.release()
cv2.destroyAllWindows()

