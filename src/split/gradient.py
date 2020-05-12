import cv2
import matplotlib.pyplot as plt

def main():
    # read a gray image
    img=cv2.imread('gradient.png',0)
    # split the threshold
    # the reback value ret is the now threshold,th is a image
    # the four parameters are the picture you want split,the threshold,the max threshold,and the thresholdTypes
    ret,th=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    cv2.imshow('th',th)
    cv2.waitKey(0)

def show_different_thresholdType():
    img=cv2.imread('gradient.png',0)

    # the five types of the threshold
    _,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    _,th2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
    _,th3=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
    _,th4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
    _,th5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

    titles = ['Original', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
    images = [img, th1, th2, th3, th4, th5]

    for i in range(6):
        plt.subplot(2,3,i+1)
        plt.imshow(images[i],'gray')
        plt.title(titles[i],fontsize=8)
        plt.xticks([]),plt.yticks([])

    plt.show()


if __name__ == '__main__':
    show_different_thresholdType()
