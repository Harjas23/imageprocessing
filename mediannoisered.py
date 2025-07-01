import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('/Users/harjasbajwa/Downloads/LH.png', cv2.IMREAD_GRAYSCALE)
median = cv2.medianBlur(img, 5)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(median, cmap='gray')
plt.title("Median Filtered Image")
plt.axis('off')
plt.tight_layout()
plt.show()