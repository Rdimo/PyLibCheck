from setuptools import setup
 
classifiers = [
  "Development Status :: 5 - Production/Stable",
  "Intended Audience :: Education",
  "Operating System :: Microsoft :: Windows :: Windows 10",
  "License :: OSI Approved :: MIT License",
  "Programming Language :: Python :: 3.9"
]
 
setup(
  name = "pylibcheck",
  version = "0.0.1",
  description = "check if a pip module is installed",
  long_description = open("README.md").read(),
  long_description_content_type = "text/markdown",
  url = "https://github.com/rdimo/pylibcheck",  
  author = "Rdimo",
  author_email = "contact.rdimo@gmail.com",
  license = "MIT", 
  keywords = "pylibcheck", 
  classifiers = classifiers,
  packages = ["pylibcheck"]
)