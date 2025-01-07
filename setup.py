from setuptools import setup, find_packages

setup(
    name="autonix",
    version="0.1.0",
    description="A lightweight framework for building autonomous agents.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Autonix",
    author_email="info@autonix.com",
    url="https://github.com/AutonixAI/Autonix",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
