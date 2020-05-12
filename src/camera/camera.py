import cv2

# if you have two or more camera ,if you want to use the second camera,just write the parameter 1 or bigger
capture=cv2.VideoCapture(0)


def main():
    #获取摄像头分辨率参数
    width,height=capture.get(3),capture.get(4)
    print(width,height)

    #使用摄像头一倍的分辨率来获取图片，如果失效一般是由于摄像头有固定的分辨率
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, width * 2)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height * 2)

    # ret is a bool to judge if something worng,get one picture
    ret,frame= capture.read()
    # turn the colorful image  to gray image
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    cv2.waitKey(0)
    cv2.imwrite('camera.jpg',gray)


if __name__ == '__main__':
    main()