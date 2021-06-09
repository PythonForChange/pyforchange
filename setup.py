from setuptools import setup, find_packages

setup(
    name = 'pyforchange',
  packages = ['pyforchange'], # this must be the same as the name above   
    include_package_data=True,    # muy importante para que se incluyan archivos sin extension .py
    version = '0.2',
    description = ' ',
    long_description= " :D ",
    author = 'Python For Change',
    author_email = 'pythonforchange@gmail.com',
    license="MIT",
    url = 'https://github.com/PythonForChange/pyforchange', # use the URL to the github repo
    download_url = 'https://github.com/PythonForChange/pyforchange/archive/v2.0.tar.gz',
    keywords = ['testing', 'logging', 'example'],
    classifiers = ['Programming Language :: Python :: 3'],
    )