import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from load_image import ft_load
from zoom import zoom_image

def rotate_image(path):
    """
    Rotates an image 90deg
    """
    try:
        # Load the image using the function from load_image.py
        img = zoom_image(path, 0.5)

        # Check the shape of the image
        print(f"Zoomed shape of the image before rotation: {img.shape}")
        print(np.array(img))

        # Rotate the zoomed image (using np.rot90 or another method)
        rotated_image = np.rot90(img)
        print(f"Shape of the image after rotation: {rotated_image.shape}")
        print(np.array(rotated_image))

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
        rotate_image('animal.jpeg')
