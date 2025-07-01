import cv2
import matplotlib.pyplot as plt

image = cv2.imread(r"C:\Users\Abhiyanshu\Downloads\WhatsApp Image 2025-06-25 at 11.09.36_f3cdd0fb.jpg")

if image is None:
    print("Error: Image not found or path is incorrect.")
    exit()

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, binary_image = cv2.threshold(gray_image, 140,255, cv2.THRESH_BINARY)


#display original to grayscale
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis('off')
plt.subplot(1,2,2)
plt.imshow(gray_image, cmap='gray')
plt.title("Grayscale Image")
plt.axis('off')
plt.tight_layout()
plt.show()


#display grayscale to binary
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.imshow(gray_image, cmap="gray")
plt.title("grayscale image")
plt.axis('off')
plt.subplot(1,2,2)
plt.imshow(binary_image, cmap='gray')
plt.title('Binary Image')
plt.axis('off')
plt.tight_layout()
plt.show()