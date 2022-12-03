import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="letitsnow",
    version="0.0.1",
    author="yavarpour",
    description="It's pip... with git.",
    long_description=long_description,
    url="https://github.com/yavarpourshahnaz/yavarpour_homework5",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)