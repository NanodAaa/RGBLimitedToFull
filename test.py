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

# 读取图像
image = cv2.imread(r'D:\NanodAaa\WORK\CMS\RGBLimitedToFull\docs\day\AMBA0005.MP4_20250120_134921.454.png')

# 获取 R, G, B 通道
r, g, b = cv2.split(image)

# 定义线性拉伸的函数
def stretch_contrast(channel, min_original, max_original, min_new, max_new):
    return np.clip(((channel - min_original) / (max_original - min_original)) * (max_new - min_new) + min_new, 0, 255)

# 拉伸每个通道
r_stretched = stretch_contrast(r, 10, 164, 0, 255)
g_stretched = stretch_contrast(g, 10, 164, 0, 255)
b_stretched = stretch_contrast(b, 10, 164, 0, 255)

# 合并通道
stretched_image = cv2.merge([r_stretched.astype(np.uint8), g_stretched.astype(np.uint8), b_stretched.astype(np.uint8)])
hist_b_full, hist_g_full, hist_r_full, ylim_full = generate_hist(stretched_image)

plt.figure(0)
plt.plot(hist_b_full, color='blue')
plt.plot(hist_g_full, color='green', linestyle='--')
plt.plot(hist_r_full, color='red', linestyle=':')
plt.xlim((0, 255))
plt.ylim((0, 10000))
plt.show()

hist_b_limited, hist_g_limited, hist_r_limited, ylim_limited = generate_hist(image)

plt.figure(1)
plt.subplot(311)
plt.plot(hist_b_full, color='blue')
plt.plot(hist_b_limited, color='b', linestyle='--')
plt.xlim((0, 255))
plt.ylim((0, 10000))
plt.subplot(312)
plt.plot(hist_g_full, color='green')
plt.plot(hist_g_limited, color='g', linestyle='--')
plt.xlim((0, 255))
plt.ylim((0, 10000))
plt.subplot(313)
plt.plot(hist_r_full, color='red')
plt.plot(hist_r_limited, color='r', linestyle='--')
plt.xlim((0, 255))
plt.ylim((0, 10000))
plt.show()

# 显示结果
cv2.imshow('Stretched Image', stretched_image)
cv2.waitKey(0)
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
