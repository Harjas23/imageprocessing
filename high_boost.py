import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread(r'C:/Users/Acer/Downloads/1000072563.jpg',0)
blurred = cv2.GaussianBlur(img,(5,5),0)
mask = cv2.subtract(img,blurred)
unsharp = cv2.add(img,mask)
k = 2.5
highbost = cv2.addWeighted(img,1.0,mask,k,0)
plt.figure(figsize=(12,5))
plt.subplot(1,3,1)
plt.imshow(blurred,cmap='grey')
plt.title("Blurred")
plt.subplot(1,3,2)
plt.imshow(unsharp,cmap='grey')
plt.subplot(1,3,3)
plt.imshow(highbost,cmap='grey')
plt.title("Highboost")
plt.tight_layout()
plt.show()