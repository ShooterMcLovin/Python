import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from load_image import ft_load

def rotate_image():
    try:
        # Load the image using the function from load_image.py
        img = ft_load("animal.jpeg")

        # Check the shape of the image
        originalShape = img.shape
        print(f"Original shape of the image: {originalShape}")

        # Zoom into the image (example slicing: slice from 100 to new height and width)
        new_height = int(originalShape[0] * 1.5)
        new_width = int(originalShape[1] * 1.5)
        zoomed_image = img[100:new_height + 125, 400:new_width + 350]
        print(f"New shape after slicing: {zoomed_image.shape}")
        print(np.array(zoomed_image))
        # Rotate the zoomed image (using np.rot90 or another method)
        rotated_image = np.rot90(zoomed_image)

        # If the image has 3 channels (RGB), convert to grayscale by averaging across channels
        if rotated_image.shape[2] == 3:
            rotated_image = np.mean(rotated_image, axis=2).astype(np.uint8)
            print("Image converted to grayscale")

        # Display the rotated (and possibly grayscale) image
        plt.imshow(rotated_image, cmap='gray' if rotated_image.ndim == 2 else None)
        plt.title("Rotated Image")
        plt.show()

        return rotated_image

    except Exception as e:
        print(f"Error: {str(e)}")
        return None


if __name__ == "__main__":
        rotate_image()
