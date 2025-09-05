# show color image to grayscale image.

import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Read the image
    img = cv2.imread("images.jpg")
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Display image + pixel grid
    plt.figure(figsize = (10, 5))
    
    plt.subplot(1, 2, 1)
    plt.imshow(gray, cmap = "gray")
    plt.title("GrayScale image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(gray, cmap = "gray")
    plt.colorbar(label = "Pixel Value")
    plt.title("Pixel Values")
    plt.show()

if __name__ == "__main__":
    main()