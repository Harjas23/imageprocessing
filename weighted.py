import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\Abhiyanshu\Downloads\DIP3E_CH03_Original_Images\DIP3E_Original_Images_CH03\Fig0333(a)(test_pattern_blurring_orig).tif",0)

kernel = np.array([[1,2,3,2,1],
                   [2,4,6,4,2],
                   [3,6,9,6,3],
                   [2,4,6,4,2],
                   [1,2,3,2,1]], dtype=np.float32)
kernel /= np.sum(kernel)
smooth_img = cv2.filter2D(img, -1 , kernel)

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(smooth_img, cmap='gray')
plt.title("Weighted Smooth Image")
plt.axis('off')
plt.tight_layout()
plt.show()