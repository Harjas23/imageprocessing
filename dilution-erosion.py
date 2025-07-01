import cv2
import numpy as np
import matplotlib.pyplot as plt

img  = cv2.imread('/Users/harjasbajwa/Downloads/LH.png', cv2.IMREAD_GRAYSCALE)

kernal = np.ones((3,3),np.uint8)
dilated = cv2.dilate(img, kernal)
eroded = cv2.erode(img, kernal)
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')
plt.subplot(1, 3, 2)
plt.imshow(dilated, cmap='gray')
plt.title("Dilated Image")
plt.axis('off')
plt.subplot(1, 3, 3)
plt.imshow(eroded, cmap='gray')
plt.title("Eroded Image")
plt.axis('off')
plt.tight_layout()
plt.show()
