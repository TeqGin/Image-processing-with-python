import cv2

def main():
    # read the image
    # imread的第二个参数表示的是选择读取的信息，0是灰度图，1是彩色图，-1是包含透明通道的彩色图
    img=cv2.imread('learn.png',0)
    # show the read image
    cv2.imshow('learn',img)

    #pause the program ks if k=0,make the program alway pause.(?)
    cv2.waitKey(0)

    # save the read image
    cv2.imwrite('learn_gray.jpg',img)

if __name__ == '__main__':
    main()