import cv2

capture=cv2.VideoCapture(0)

# 指定编码方式并创建一个VideoWriter对象
# 这是MJPG编码
fourcc =cv2.VideoWriter_fourcc(*'MJPG')
# the four parameters  are output file name, fourcc which the way to encode,FPS and Resolution(分辨率)
outfile=cv2.VideoWriter('outfile.avi',fourcc,25,(640,480))


def main():
    # record the video until the camera close
    while(capture.isOpened()):
        # get one every frame
        ret,frame=capture.read()

        # if the camera is normal and you successfully open the camera
        if ret:
            # wirte dowm every frame
            outfile.write(frame)
            cv2.imshow('frame',frame)
            if cv2.waitKey(1)==ord('q'):
                break
        else:
            break

if __name__ == '__main__':
    main()