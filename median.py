import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\Abhiyanshu\Downloads\DIP3E_CH03_Original_Images\DIP3E_Original_Images_CH03\Fig0335(a)(ckt_board_saltpep_prob_pt05).tif",0)

median_3 = cv2.medianBlur(img, 3)
median_5 = cv2.medianBlur(img, 5)

plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')
plt.subplot(1, 3, 2)
plt.imshow(median_3, cmap='gray')
plt.title("Median (3x3) Image")
plt.axis('off')
plt.subplot(1, 3, 3)
plt.imshow(median_5, cmap='gray')
plt.title("Median (5x5) Image")
plt.axis('off')
plt.tight_layout()
plt.show()