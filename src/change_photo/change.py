import cv2


def main():
    img=cv2.imread('learn.png')

    # 获取RGB色彩值
    # the parameters are y and x
    px=img[100,90]
    print(px)

    # 获取蓝色通道的色彩值
    px_blue=img[100,90,0]
    print(px_blue)

    # 修改某个点的像素色彩值,只是这样写无法修改原图，智能修改内存中的值
    img[100,90]=[255,255,255]
    print(img[100,90])

    # reback three parameters,行数，列数，通道数
    height,width,channels=img.shape
    print(img.shape)

    # reback the datetype of the image
    print(img.dtype)

    # reback the all pixels
    print(img.size)


if __name__ == '__main__':
    main()