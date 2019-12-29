from setuptools import setup

setup(
  name="clisales",
  version="0.1",
  author="Esteban Solorzano",
  py_modules=["clisales"],
  install_requires=[
    "Click"
  ],
  entry_points={
    "console_scripts": [
      "clisales = main:cli"
    ]
  }
)