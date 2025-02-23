from setuptools import setup, find_packages

setup(
    name="writer_markdown",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="Harsh Gupta",
    author_email="guptaharshbly@gmail.com",
    description="A simple Python library to generate Markdown files.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/4444Harsh/Writer_Markdown.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
