import cv2

capture =cv2.VideoCapture('laugh.mp4')

def main():
    while(True):
        # read every frame in the video
        ret,frame=capture.read()
        # turn to gray image
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # show
        cv2.imshow('frame',gray)
        # to make the video play  fluently, k alway set 30 or 25
        if cv2.waitKey(30)== ord('q'):
            break

# don't forget to write this
if __name__ == '__main__':
    main()