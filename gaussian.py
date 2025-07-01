import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\Abhiyanshu\Downloads\DIP3E_CH02_Original_Images\DIP3E_Original_Images_CH02\Fig0219(rose1024).tif",0)

gauss_5x5 = cv2.GaussianBlur(img, (5,5), 0)
gauss_15x15 = cv2.GaussianBlur(img, (15,15), 0)

plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')
plt.subplot(1, 3, 2)
plt.imshow(gauss_5x5, cmap='gray')
plt.title("Gaussian (5x5) Image")
plt.axis('off')
plt.subplot(1, 3, 3)
plt.imshow(gauss_15x15, cmap='gray')
plt.title("Gaussian (15x15) Image")
plt.axis('off')
plt.tight_layout()
plt.show()