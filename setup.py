from setuptools import setup, find_packages

setup(
    name="omnishift",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "Pillow>=9.0.0",
    ],
    entry_points={
        "console_scripts": [
            "omnishift=omnishift.cli:main",
        ],
    },
    author="Ishaan S. Oshima",
    author_email="ishaansoshima@gmail.com",
    description="A CLI tool for converting images between different formats",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/omnishift",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)