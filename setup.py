"""Setup configuration for optimization toolkit."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="optimization-toolkit",
    version="0.1.0",
    author="Optimization Toolkit Contributors",
    description="A comprehensive toolkit for optimization algorithms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abrigandi/optimization",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "numpy>=1.20.0",
        "scipy>=1.7.0",
    ],
)
