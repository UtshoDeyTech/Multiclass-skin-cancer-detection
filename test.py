import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_rgb_histograms(original_img, normalized_img):
    colors = ('b', 'g', 'r')
    plt.figure(figsize=(15, 5))
    
    # Original image histograms
    plt.subplot(121)
    for i, color in enumerate(colors):
        hist = cv2.calcHist([original_img], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
    plt.title('Original RGB Histograms')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    
    # Normalized image histograms
    plt.subplot(122)
    for i, color in enumerate(colors):
        hist = cv2.calcHist([normalized_img], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
    plt.title('Normalized RGB Histograms')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    
    plt.tight_layout()
    plt.show()

# Read and process image
img = cv2.imread('your_image.jpg')
normalized_img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)

# Display RGB histograms
plot_rgb_histograms(img, normalized_img)

# Optional: Display images
cv2.imshow('Original Image', img)
cv2.imshow('Normalized Image', normalized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()