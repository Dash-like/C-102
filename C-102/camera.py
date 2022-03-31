import random
import cv2
import string
def takesnapshot():
    videocapture = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = videocapture.read()
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))
        cv2.imwrite(str(str(res) + ".jpg"), frame)
        result = False
    videocapture.release()
    cv2.destroyAllWindows()
takesnapshot()
    
    # a,b = 0, 1
