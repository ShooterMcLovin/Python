import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from load_image import ft_load

def ft_invert(array):
    # """
    # Reverses the color of an image
    # """
    img = ft_load("landscape.jpeg")
    # Invert the image (255 - pixel values) for RGB images
    img_inverted = 255 - img
    # Display the inverted image without converting to grayscale
    plt.imshow(img_inverted)
    plt.title("Inverted Image")
    plt.show()    


def ft_red(array):
    # """
    # Turns image red
    # """
    img = ft_load("landscape.jpeg")
    if img.shape[2] == 3:
        img = np.mean(img, axis=2).astype(np.uint8)
    plt.imshow(img, cmap='Reds' if img.ndim == 2 else None)
    plt.title("Red Image")
    plt.show()

def ft_green(array):
    # """
    # Turns image green
    # """
    img = ft_load("landscape.jpeg")
    if img.shape[2] == 3:
        img = np.mean(img, axis=2).astype(np.uint8)
    plt.imshow(img, cmap='Greens' if img.ndim == 2 else None)
    plt.title("Green Image")
    plt.show()

def ft_blue(array):
    # """
    # Turns image blue
    # """
    img = ft_load("landscape.jpeg")
    if img.shape[2] == 3:
        img = np.mean(img, axis=2).astype(np.uint8)
    plt.imshow(img, cmap='Blues' if img.ndim == 2 else None)
    plt.title("Blue Image")
    plt.show()

def ft_grey(array):
    # """
    # Turns image to grayscale
    # """
    img = ft_load("landscape.jpeg")
    if img.shape[2] == 3:
        img = np.mean(img, axis=2).astype(np.uint8)
    plt.imshow(img, cmap='grey' if img.ndim == 2 else None)
    plt.title("Grayscale Image")
    plt.show()
