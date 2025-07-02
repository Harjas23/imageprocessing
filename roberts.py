import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread(r'C:/Users/Acer/Downloads/1000072563.jpg',0)

kernel_roberts_x = np.array([[1,0],[0,-1]])
kernel_roberts_y = np.array([[0,1],[-1,0]])
gx = cv2.filter2D(img,-1,kernel_roberts_x)
gy = cv2.filter2D(img,-1,kernel_roberts_y)
roberts = cv2.magnitude(gx.astype(float),gy.astype(float))
plt.imshow(roberts,cmap='grey')
plt.title("Roberts")
plt.show()