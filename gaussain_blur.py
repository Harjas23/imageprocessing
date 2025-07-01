import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/Users/harjasbajwa/Downloads/LH.png', cv2.IMREAD_GRAYSCALE)
gaussian_blur = cv2.GaussianBlur(img, (5, 5), 0)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(gaussian_blur, cmap='gray')
plt.title("Gaussian Blurred Image")
plt.axis('off')
plt.tight_layout()
plt.show()
