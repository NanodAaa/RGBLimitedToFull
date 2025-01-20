# RGBLimitedToFull.py

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def generate_hist(image_bgr):
    """ 
    Generate Hist of BGR (RGB888).
    
    `image_bgr`: Image array (numpy).
    Return: Array of hist B, G, R; Maximum value of y-axis.
    """
    
    hist_b = cv2.calcHist([image_bgr], [0], None, [256], [0, 256])
    hist_g = cv2.calcHist([image_bgr], [1], None, [256], [0, 256])
    hist_r = cv2.calcHist([image_bgr], [2], None, [256], [0, 256])
    ylim_array = [np.max(hist_b), np.max(hist_g), np.max(hist_r)]
    ylim = int(np.max(ylim_array))
    
    return hist_b, hist_g, hist_r, ylim
    
def range_limited2full(image_limited, lower_limit, upper_limit):
    """ 
    Mapping limited range bgr to full range bgr (RGB888).
    
    `image_limited`: Image limited range array (numpy).
    """
    
    image_limited = image_limited.astype(np.float32)
    
    # Formula 0
#    image_full = (image_limited - lower_limit) / (upper_limit - lower_limit) * 255
    # Formula 1
    image_full = ((255 - 0) / (upper_limit - lower_limit)) * (image_limited - lower_limit) + 0
    
    image_full = np.clip(image_full, 0, 255)
    image_full = image_full.astype(np.uint8)

    return image_full

if __name__ == '__main__':
    IMAGE_PATH = r'D:\NanodAaa\WORK\CMS\RGBLimitedToFull\docs\day\AMBA0005.MP4_20250120_134921.454.png'
    LIMITED_RANGE = (30, 240)
    
    image_limited = cv2.imread(IMAGE_PATH)
    image_full = range_limited2full(image_limited, LIMITED_RANGE[0], LIMITED_RANGE[1])
    image_full_path = os.path.join(os.path.dirname(IMAGE_PATH), os.path.splitext(os.path.basename(IMAGE_PATH))[0] + '-full' + os.path.splitext(os.path.basename(IMAGE_PATH))[1])   
    cv2.imwrite(image_full_path, image_full)
    """ cv2.imshow('Image Limited Range', image_limited)
    cv2.imshow('Image Full Range', image_full)
    cv2.waitKey(0) """
    
    hist_b_limited, hist_g_limited, hist_r_limited, ylim_limited = generate_hist(image_limited)
    hist_b_full, hist_g_full, hist_r_full, ylim_full = generate_hist(image_full)
    
    plt.figure(0)
    plt.subplot(321)
    plt.plot(hist_b_limited, color='blue', label='B Channel')
    plt.xlim([0, 256])
    plt.ylim([0, ylim_limited])
    
    plt.subplot(323)
    plt.plot(hist_g_limited, color='green', label='G Channel')
    plt.xlim([0, 256])
    plt.ylim([0, ylim_limited])
    
    plt.subplot(325)
    plt.plot(hist_r_limited, color='red', label='R Channel')
    plt.xlim([0, 256])
    plt.ylim([0, ylim_limited])
    
    plt.subplot(322)
    plt.plot(hist_b_full, color='blue', label='B Channel')
    plt.xlim([0, 256])
    plt.ylim([0, ylim_limited])
    
    plt.subplot(324)
    plt.plot(hist_g_full, color='green', label='G Channel')
    plt.xlim([0, 256])
    plt.ylim([0, ylim_limited])
    
    plt.subplot(326)
    plt.plot(hist_r_full, color='red', label='R Channel')
    plt.xlim([0, 256])
    plt.ylim([0, ylim_limited])
    
    plt.show()
    