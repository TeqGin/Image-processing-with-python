import cv2

capture=cv2.VideoCapture(0)

def main():
    #获取一帧图片
    ret,frame= capture.read()
    # 转化为灰度图
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    cv2.waitKey(0)
    cv2.imwrite('camera.jpg',gray)

if __name__ == '__main__':
    main()