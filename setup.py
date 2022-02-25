from setuptools import setup, find_packages

__name__ = "pylibcheck"
__version__ = "0.2.1"

setup(
    name=__name__,
    version=__version__,
    author="Rdimo",
    author_email="<contact.rdimo@gmail.com>",
    description="Simple library to check if packages are installed and install them for you",
    long_description_content_type="text/markdown",
    long_description=open("README.md", encoding="utf-8").read(),
    url = "https://github.com/rdimo/pylibcheck",
    project_urls={
      "Bug Tracker": "https://github.com/rdimo/pylibcheck/issues",
    },
    packages=find_packages(),
    keywords=['pylibcheck', 'python', 'package', 'library', 'lib', 'module', 'checker'],
    classifiers=[
      "Intended Audience :: Developers",
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
    ]
)