from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
Loads an image and returns its pixel information as an numpy array
    """
    try:
        img = Image.open(path)
        print(f"The format of the image is: {img.format}")

        # Convert the image to RGB mode if not already in RGB
        img_rgb = img.convert('RGB')

        # Get the pixel data as a NumPy array
        pixels = np.array(img_rgb)

        # Print the shape of the image and the pixel data
        print(f"The shape of the image is: {pixels.shape}")
        print(pixels)

        return pixels

    except FileNotFoundError:
        print(f"Error: The file at path '{path}' was not found.")
    except IOError:
        print(f"Error: The file at path '{path}' " +
              "is not a valid image or is unsupported.")
    except Exception as e:
        print(f"Error: {e}")
    return None
