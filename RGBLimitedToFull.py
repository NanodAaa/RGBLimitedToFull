# RGBLimitedToFull.py

import cv2
import numpy as np
import matplotlib.pyplot as plt

def generate_hist(image_path):
    """ 
    Generate Hist of BGR.
    
    `image_path`: Image Path.
    Return: Array of hist B, G, R; Maximum value of y-axis.
    """
    image_bgr = cv2.imread(image_path)
    hist_b = cv2.calcHist([image_bgr], [0], None, [256], [0, 256])
    hist_g = cv2.calcHist([image_bgr], [1], None, [256], [0, 256])
    hist_r = cv2.calcHist([image_bgr], [2], None, [256], [0, 256])
    ylim_array = [np.max(hist_b), np.max(hist_g), np.max(hist_r)]
    ylim = int(np.max(ylim_array))
    
    return hist_b, hist_g, hist_r, ylim
    
def range_limited2full(image_path):
    
    return


if __name__ == '__main__':
    IMAGE_PATH = r'D:\NanodAaa\WORK\CMS\RGBLimitedToFull\docs\day\AMBA0005.MP4_20250120_134921.454.png'
    
    image_bgr = cv2.imread(IMAGE_PATH)
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    r, g, b = cv2.split(image_rgb)
    image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
    
    hist_b, hist_g, hist_r, ylim = generate_hist(IMAGE_PATH)
    plt.figure(0)
    plt.subplot(311)
    plt.plot(hist_b, color='blue', label='B Channel')
    plt.xlim([0, 256])
    plt.ylim([0, ylim])
    
    plt.subplot(312)
    plt.plot(hist_g, color='green', label='G Channel')
    plt.xlim([0, 256])
    plt.ylim([0, ylim])
    
    plt.subplot(313)
    plt.plot(hist_r, color='red', label='R Channel')
    plt.xlim([0, 256])
    plt.ylim([0, ylim])
    
    plt.show()
    
    exit()
    cv2.imshow('Image BGR', image_bgr)
    cv2.waitKey(0)
    cv2.imshow('Image Gray', image_gray)
    
    