import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread(r'C:/Users/Acer/Downloads/1000072563.jpg',0)
laplacian = np.array([[0,1,0],[1,-4,1],[0,1,0]])

lapimg = cv2.filter2D(img,-1,laplacian)
img1 = img - lapimg
plt.figure(figsize=(10,5))
plt.subplot(1,3,1)
plt.imshow(img,cmap='grey')
plt.title('ORIGNAL IMAGE')
plt.subplot(1,3,2)
plt.imshow(lapimg,cmap='grey')
plt.title("Lplancian")
plt.subplot(1,3,3)
plt.imshow(img1,cmap='grey')
plt.title("Enhanced")
plt.tight_layout()
plt.show()