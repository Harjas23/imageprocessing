import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\Abhiyanshu\Downloads\DIP3E_CH02_Original_Images\DIP3E_Original_Images_CH02\Fig0232(a)(partial_body_scan).tif", cv2.IMREAD_GRAYSCALE)

enhanced = img.astype(np.float32)*1.5
enhanced = np.clip(enhanced,0,255).astype('uint8')

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(enhanced, cmap='gray')
plt.title("Contrast Enhanced Image")
plt.axis('off')
plt.tight_layout()
plt.show()