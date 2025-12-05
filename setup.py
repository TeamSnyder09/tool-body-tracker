from setuptools import setup, find_packages

setup(
    name="tool-body-tracker",
    version="1.0.0",
    description="A program to track tool body time installed on machines",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "click>=8.1.0",
        "tabulate>=0.9.0",
    ],
    entry_points={
        "console_scripts": [
            "tool-tracker=src.cli:main",
        ],
    },
    python_requires=">=3.8",
)
