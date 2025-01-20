# RGBLimitedToFull.py

import cv2
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    IMAGE_PATH = r'D:\DOWNLOAD\CHROME_SAVE\thumb-lite.png'
    
    image_bgr = cv2.imread(IMAGE_PATH)
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    r, g, b = cv2.split(image_rgb)
    image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
    
    hist_r = cv2.calcHist([image_rgb], [0], None, [256], [0, 256])
    hist_g = cv2.calcHist([image_rgb], [1], None, [256], [0, 256])
    hist_b = cv2.calcHist([image_rgb], [2], None, [256], [0, 256])
    
    
    plt.figure(0)
    plt.subplot(311)
    plt.plot(hist_r, color='red', label='R Channel')
    plt.xlim([0, 256])
    plt.ylim([0, 100000])
    
    plt.subplot(312)
    plt.plot(hist_g, color='green', label='G Channel')
    plt.xlim([0, 256])
    plt.ylim([0, 100000])
    
    plt.subplot(313)
    plt.plot(hist_b, color='blue', label='B Channel')
    plt.xlim([0, 256])
    plt.ylim([0, 100000])
    
    plt.show()
    
    exit()
    cv2.imshow('Image BGR', image_bgr)
    cv2.waitKey(0)
    cv2.imshow('Image Gray', image_gray)
    
    