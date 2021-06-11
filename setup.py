from setuptools import setup, find_packages
import pathlib
HERE = pathlib.Path(__file__).parent
README1 = (HERE / 'README.md').read_text()
README2 = (HERE / 'README.rst').read_text()

setup(
    name = 'pyforchange',
  packages = ['pyforchange'], # this must be the same as the name above   
    include_package_data=True,    # muy importante para que se incluyan archivos sin extension .py
    version = '2.0.2',
    description ="pythonforchange.github.io",
    long_description=README1,
    long_description_content_type='text/markdown',
    author = 'Python For Change',
    author_email = 'pythonforchange@gmail.com',
    license="MIT",
    url = 'https://github.com/PythonForChange/pyforchange', # use the URL to the github repo
    download_url = 'https://github.com/PythonForChange/pyforchange/archive/refs/tags/v2.0.2.tar.gz',
    keywords = ['covid', 'logging', 'language', 'plot', 'life'],
    classifiers = ['Programming Language :: Python :: 3'],
    )