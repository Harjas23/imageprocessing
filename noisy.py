import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\Abhiyanshu\OneDrive\Pictures\Screenshots\Screenshot 2025-06-18 112850.png",cv2.IMREAD_GRAYSCALE)

noisy_img = img.copy()
rows, cols = img.shape
num_noisy_pixels = 5000
for _ in range(num_noisy_pixels):
    x,y = np.random.randint(0,rows), np.random.randint(0,cols)
    noisy_img[x,y] = np.random.choice([0.255])

shift1 = np.roll(noisy_img, 1, axis=0)
shift2 = np.roll(noisy_img, -1, axis=0)
shift3 = np.roll(noisy_img, 1, axis=1)
shift4 = np.roll(noisy_img, -1, axis=1)

smoothed = (noisy_img.astype(np.float32) + shift1 + shift2 + shift3 + shift4) / 5.0
smoothed = np.clip(smoothed,0,255).astype(np.uint8)

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.imshow(noisy_img,cmap='gray')
plt.title("Noisy Image")
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(smoothed, cmap='gray')
plt.title("Smoothed Image")
plt.axis('off')
plt.tight_layout()
plt.show()



############################################################################################################


# def add_noise(img, num_pixels=2000 ):
#     noisy = img.copy()
#     rows,cols = noisy.shape
#     for _ in range(num_pixels):
#         x,y = np.random.randint(0,rows), np.random.randint(0,cols)
#         noisy[x,y] = np.random.choice([0.255])
#     return noisy

# def smooth_with_neighbourhood(img,ksize):
#     half = ksize//2
#     img = img.astype(np.float32)
#     total = np.zeros_like(img,dtype=np.float32)
#     count = 0

#     for dx in range(-half,half+1):
#         for dy in range(-half, half+1):
#             shifted = np.roll(np.roll(img,dx,axis=0) , dy, axis=1)
#             total += shifted
#             count += 1

#     avg = total/count
#     return np.clip(avg,0,255).astype(np.uint8)

# noisy_img = add_noise(img,num_pixels=10000)

# smoothed3 = smooth_with_neighbourhood(noisy_img,3)
# smoothed5 = smooth_with_neighbourhood(noisy_img,5)
# smoothed7 = smooth_with_neighbourhood(noisy_img,9)
# smoothed15 = smooth_with_neighbourhood(noisy_img,15)

# titles = ['Noisy Image', 'Smoothed (3x3)', 'Smoothed (5x5)', 'Smoothed (7x7)', 'Smoothed (15x15)']
# results = [smoothed3, smoothed5, smoothed7, smoothed15]

# for i in range(4):
#     plt.figure(figsize=(12,5))
#     plt.subplot(1, 2, 1)
#     plt.imshow(noisy_img, cmap='gray')
#     plt.title("Noisy Image")
#     plt.axis('off')
#     plt.subplot(1, 2, 2)
#     plt.imshow(results[i], cmap='gray')
#     plt.title(f"Smoothed Image {titles[i+1]}")
#     plt.axis('off')
#     plt.tight_layout()
#     plt.show()
