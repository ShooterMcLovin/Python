import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from load_image import ft_load

def ft_invert(array):
    img = ft_load("landscape.jpeg")
    # Invert the image (255 - pixel values) for RGB images
    img_inverted = 255 - img
    # Display the inverted image without converting to grayscale
    plt.imshow(img_inverted)
    plt.title("Inverted Image")
    plt.show()    


def ft_red(array):
    img = ft_load("landscape.jpeg")
    if img.shape[2] == 3:
        img = np.mean(img, axis=2).astype(np.uint8)
    plt.imshow(img, cmap='Reds' if img.ndim == 2 else None)
    plt.show()

def ft_green(array):
    img = ft_load("landscape.jpeg")
    if img.shape[2] == 3:
        img = np.mean(img, axis=2).astype(np.uint8)
    plt.imshow(img, cmap='Greens' if img.ndim == 2 else None)
    plt.show()

def ft_blue(array):
    img = ft_load("landscape.jpeg")
    if img.shape[2] == 3:
        img = np.mean(img, axis=2).astype(np.uint8)
    plt.imshow(img, cmap='Blues' if img.ndim == 2 else None)
    plt.show()

def ft_grey(array):
    img = ft_load("landscape.jpeg")
    if img.shape[2] == 3:
        img = np.mean(img, axis=2).astype(np.uint8)
    plt.imshow(img, cmap='grey' if img.ndim == 2 else None)
    plt.show()
