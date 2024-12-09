import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from load_image import ft_load, slice_me

def zoom_image(path, zoom_factor) -> np.ndarray:
    """
    Zoom on an image by slicing
    """
    try:
        # Get the original shape
        img = ft_load(path)
        original_shape = img.shape
        new_height = int(original_shape[0] * zoom_factor)
        new_width = int(original_shape[1] * zoom_factor)

        zoomed_image = img[100 :new_height + 125, 400:new_width + 350]

        # Display the new shape after zooming
        print(f"New shape after slicing: {zoomed_image.shape}")
        print((zoomed_image))
        # if zoomed_image.shape[2] == 3:
            # zoomed_image = np.mean(zoomed_image, axis=2).astype(np.uint8)
            # print("Image converted to grayscale")

        # plt.imshow(zoomed_image, cmap='gray' if zoomed_image.ndim == 2 else None)
        # plt.show()

        return zoomed_image

    except IndexError as e:
        print(f"Error: Could not zoom into the image. {str(e)}")
        return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

if __name__ == "__main__":
    try:

        # Perform zoom operation
        zoom_image(path='animal.jpeg', zoom_factor=0.5)

    except FileNotFoundError:
        print("Error: 'animal.jpeg' file not found. Please check the file path.")
    except Exception as e:
        print(f"Error: {str(e)}")
