import cv2
import numpy as np
import matplotlib.pyplot as plt

img  = cv2.imread('/Users/harjasbajwa/Downloads/LH.png', cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Image not found.")
else:
    print("Image loaded successfully.")
    cv2.imshow("Original Image", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

enhanced = img.astype(np.float32)*1.5
enhanced = np.clip(enhanced, 0, 255).astype(np.uint8)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(enhanced, cmap='gray')
plt.title("Enhanced Image")
plt.axis('off')
plt.tight_layout()
plt.show()