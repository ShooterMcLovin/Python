from setuptools import setup, find_packages

setup(
    name="ft_package",
    version="0.0.1",
    packages=find_packages(),
    description="A sample test package",
    author="eagle",
    author_email="eagle@42.fr",
    url="https://github.com/eagle/ft_package",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)