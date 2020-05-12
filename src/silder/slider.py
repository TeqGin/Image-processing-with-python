import cv2
import numpy as np


def nothing(x):
    pass


def main():
    # creat a white picture
    img=np.zeros((300, 512, 3), np.uint8)
    cv2.namedWindow('image')

    # the five parameter means name of the slider 、the window's name which the slider belongs、
    # the value at beginning、the max number 、a callback function which has a default parameter which is current value
    cv2.createTrackbar('R','image',0,255,nothing)
    cv2.createTrackbar('G','image',0,255,nothing)
    cv2.createTrackbar('B','image',0,255,nothing)

    while(True):
        cv2.imshow('image',img)
        if cv2.waitKey(1)==27:
            break

        #get the current value
        r = cv2.getTrackbarPos('R','image')
        g = cv2.getTrackbarPos('G', 'image')
        b = cv2.getTrackbarPos('B', 'image')
        # reset the slider's value
        img[:]=[b,g,r]


if __name__ == '__main__':
    main()