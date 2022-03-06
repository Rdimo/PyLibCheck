<p align="center">
  <img src="https://img.shields.io/pypi/v/PyLibCheck?style=flat-square" </a>
  <img src="https://img.shields.io/pypi/l/PyLibCheck?style=flat-square" </a>
  <img src="https://img.shields.io/pypi/dm/pylibcheck?style=flat-square" </a>
  <img src="https://img.shields.io/github/stars/Rdimo/PyLibCheck?label=Stars&style=flat-square" </a>
  <img src="https://img.shields.io/github/forks/Rdimo/PyLibCheck?label=Forks&style=flat-square" </a>
</p>

#### PyLibCheck was made by
Love ❌ code ✅

---
### 🎈・Code example
Example of how you can use [pylibcheck](https://pypi.org/project/pylibcheck/)
```py
import pylibcheck, time

if not pylibcheck.checkPackage("pyinstaller"):
    print("pyinstaller is not installed!")
    time.sleep(1)
    print("installing it for you!")
    pylibcheck.installPackage("pyinstaller")
```
