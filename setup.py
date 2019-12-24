from setuptools import setup, find_packages

with open("README.md", "r") as ff:
    long_description = ff.read()

setup(
    name="example-pkg-tonychoucc",
    version="0.0.3",
    author="Tony Chou",
    author_email="cool21540125@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cool21540125/demo_pypi",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
