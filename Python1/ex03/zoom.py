import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def zoom_image(path, zoom_factor) -> np.ndarray:
    """
This function zooms on the middle of the image
def zoom_image(path, zoom_factor) -> np.ndarray:
    Where:
        Path is a str of the where the image is
        zoom_factor is the factor by wich the image is zoomed:
         1 means original size and 0.5 is half the original size
    Note: valid entries are 0.1 to 1
    """
    try:
        if zoom_factor < 0.1 or zoom_factor > 1:
            raise Exception("Invalid zoom factor, valid entries are 0.1 to 1")

        img = ft_load(path)
        if img is None:
            return
        original_shape = img.shape
        # Calculate new shape based on zoom factor
        new_height = int(original_shape[0] * zoom_factor)
        new_width = int(original_shape[1] * zoom_factor)

        # Calculate the top-left corner of the zoomed region to center it
        start_y = int(original_shape[0] / 2) - int(new_height / 2)
        end_y = start_y + new_height

        start_x = int(original_shape[1] / 2) - int(new_width / 2)
        end_x = start_x + new_width

        # Slice the image to zoom into the center
        zoomed_image = img[start_y:end_y, start_x:end_x, :1]

        print(f"New shape after slicing: {zoomed_image.shape}")
        print(np.array(zoomed_image))
        # convert to grayscale
        if zoomed_image.shape[2]:
            zoomed_image = np.mean(zoomed_image, axis=2).astype(np.uint8)
            print("Image converted to grayscale")

        # Display the zoomed image with axes
        if zoomed_image.ndim == 2:
            plt.imshow(zoomed_image, cmap='gray')
        plt.show()

        return zoomed_image

    except IndexError as e:
        print(f"Error: Could not zoom into the image. {str(e)}")
        return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None


if __name__ == "__main__":
    try:
        zoom_image(path='animal.jpeg', zoom_factor=0.5)

    except FileNotFoundError:
        print("Error: 'animal.jpeg' file not found. Check the file path.")
    except Exception as e:
        print(f"Error: {str(e)}")
