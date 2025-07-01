import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\Abhiyanshu\Downloads\DIP3E_CH03_Original_Images\DIP3E_Original_Images_CH03\Fig0335(a)(ckt_board_saltpep_prob_pt05).tif",0)

kernel = np.ones((3,3),np.uint8)
min_img = cv2.erode(img, kernel)
max_img = cv2.dilate(img, kernel)
median_img = cv2.medianBlur(img,3)


plt.subplot(1, 4, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')
plt.subplot(1, 4, 2)
plt.imshow(min_img, cmap='gray')
plt.title("Minimum Image")
plt.axis('off')
plt.subplot(1, 4, 3)
plt.imshow(max_img, cmap='gray')
plt.title("Maximum Image")
plt.axis('off')
plt.subplot(1, 4, 4)
plt.imshow(median_img, cmap='gray')
plt.title("Median Image")
plt.axis('off')
plt.tight_layout()
plt.show()