import cv2

def main():
    img=cv2.imread('learn.png')
    # cut the picture
    part=img[100:300,100:500]
    # cv2.imshow('part',part)
    # cv2.waitKey(0)

    # 彩色图的BGR三个通道可以分开访问，也可以合在一起
    b,g,r=cv2.split(img)
    # or the third paramter can be [-3,2]
    _b=img[:,:,0]
    cv2.imshow('blue',_b)
    cv2.waitKey(0)

    img=cv2.merge((b,g,r))
    # cv2.imshow('img',img)
    # cv2.waitKey(0)

if __name__ == '__main__':
    main()