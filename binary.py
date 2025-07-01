import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/Users/harjasbajwa/Downloads/LH.png', cv2.COLOR_RGB2GRAY)
_,bin = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(bin, cmap='gray')
plt.title("Binary Image")
plt.axis('off')
plt.tight_layout()
plt.show()
    