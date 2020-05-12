import cv2
import numpy as np

capture =cv2.VideoCapture(0)
# set the lower range of the blue
lower_blue=np.array([100,110,110])
# set the height range of the blue
height_blue=np.array([130,255,255])

# set the lower range of the red
lower_red=np.array([0,110,110])
# set the height range of the red
height_red=np.array([10,255,255])

def main():
    img=cv2.imread('catchColor.png')
    # turn into gray image
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    cv2.imshow('img',img)
    cv2.imshow('img_gray',img_gray)
    cv2.waitKey(0)

def catch_color():
    while(True):
        # read one frame
        ret,frame=capture.read()
        # turn into hsv model
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        # inRange if the color is in lower to height ,it will be white
        mask=cv2.inRange(hsv,lower_blue,height_blue)
        # only save the part which color is blue
        res=cv2.bitwise_and(frame,frame,mask=mask)

        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)
        # if you enter the 'q',then quit the program
        if cv2.waitKey(1)==ord('q'):
            break

def get_hsv_range():
    # remenber the parameter is B(blue) G(green) R(red)
    blue=np.uint8([[[0,0,255]]])
    hsv_blue=cv2.cvtColor(blue,cv2.COLOR_BGR2HSV)
    print(hsv_blue)

if __name__ == '__main__':
    catch_color()