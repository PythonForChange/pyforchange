from distutils.core import setup
setup(
  name = 'pyforchange',
  packages = ['pyforchange'], # this must be the same as the name above
  version = '0.1',
  description = 'my description',
  author = 'Python For Change',
  author_email = 'pythonforchange@gmail.com',
  url = 'https://github.com/PythonForChange/pyforchange', # use the URL to the github repo
  download_url = 'https://github.com/PythonForChange/pyforchange/tarball/0.1',
  keywords = ['testing', 'logging', 'example'],
  classifiers = [],
)
from setuptools import setup, find_packages

setup(
    name = 'pyforchange',
  packages = ['pyforchange'], # this must be the same as the name above   
    include_package_data=True,    # muy importante para que se incluyan archivos sin extension .py
    version = '0.1',
    description = ' ',
    author = 'Python For Change',
    author_email = 'pythonforchange@gmail.com',
    license="MIT",
    url = 'https://github.com/PythonForChange/pyforchange', # use the URL to the github repo
    download_url = 'https://github.com/PythonForChange/pyforchange/tarball/0.1',
    keywords = ['testing', 'logging', 'example'],
    classifiers = ["Programming Language :: Python :: 3",\
        "License :: MIT",\
        "Development Status :: 1 - Beta", "Intended Audience :: Developers", \
        "Operating System :: OS Independent"],
    )