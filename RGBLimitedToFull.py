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
    
def range_limited2full(image_limited, lower_limit, upper_limit, lower_full, upper_full):
    """ 
    Mapping limited range bgr to full range bgr (RGB888).
    
    `image_limited`: Image limited range array (numpy).
    """
    
    image_limited = image_limited.astype(np.float32)
    
    # Formula 0
#    image_full = (image_limited - lower_limit) / (upper_limit - lower_limit) * 255
    # Formula 1
    image_full = ((upper_full - lower_full) / (upper_limit - lower_limit)) * (image_limited - lower_limit) + lower_full
    
    image_full = np.clip(image_full, lower_full, upper_full)
    image_full = image_full.astype(np.uint8)

    return image_full

if __name__ == '__main__':
    IMAGE_PATH = r'D:\NanodAaa\WORK\CMS\RGBLimitedToFull\docs\night\AMBA0004.MP4_20250120_135228.821.png'
    FULL_RANGE = (0, 255)
    LIMITED_RANGE = (10, 165)
    
    image_limited = cv2.imread(IMAGE_PATH)
    cv2.imshow('Image Limited Range', image_limited)
    hist_b_limited, hist_g_limited, hist_r_limited, ylim_limited = generate_hist(image_limited)
    
    image_gray = cv2.cvtColor(image_limited, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Image Gray', image_gray)
    
    limited_range = (np.min(image_gray), np.max(image_gray))
    limited_range = LIMITED_RANGE
    print(limited_range)
    
    image_full = range_limited2full(image_limited, limited_range[0], limited_range[1], FULL_RANGE[0], FULL_RANGE[1])
    cv2.imshow('Image Full Range', image_full)
    hist_b_full, hist_g_full, hist_r_full, ylim_full = generate_hist(image_full)
    image_full_path = os.path.join(os.path.dirname(IMAGE_PATH), os.path.splitext(os.path.basename(IMAGE_PATH))[0] + '-full' + os.path.splitext(os.path.basename(IMAGE_PATH))[1])
    cv2.imwrite(image_full_path, image_full)
    
    plt.figure(0)
    plt.subplot(311)
    plt.plot(hist_b_limited, color='blue', label='B Channel', linestyle='--')
    plt.plot(hist_b_full, color='blue', label='B Channel')
    plt.xlim(FULL_RANGE)
    plt.ylim([0, ylim_limited])
    
    plt.subplot(312)
    plt.plot(hist_g_limited, color='green', label='G Channel', linestyle='--')
    plt.plot(hist_g_full, color='green', label='G Channel')
    plt.xlim(FULL_RANGE)
    plt.ylim([0, ylim_limited])
    
    plt.subplot(313)
    plt.plot(hist_r_limited, color='red', label='R Channel', linestyle='--')
    plt.plot(hist_r_full, color='red', label='R Channel')
    plt.xlim(FULL_RANGE)
    plt.ylim([0, ylim_limited])

    figure_path_hist = os.path.join(os.path.dirname(IMAGE_PATH), os.path.splitext(os.path.basename(IMAGE_PATH))[0] + '-hist' + os.path.splitext(os.path.basename(IMAGE_PATH))[1])
    plt.savefig(figure_path_hist)
    plt.show()
    