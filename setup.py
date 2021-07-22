from setuptools import setup, find_packages
import pathlib
HERE = pathlib.Path(__file__).parent
README1 = (HERE / 'README.md').read_text()
README2 = (HERE / 'README.rst').read_text()

setup(
    name = 'pyforchange',
    packages=find_packages(),
    install_requires=['pandas','os','time','json','math', 'sys', 'subprocess', 'pip', 'bs4'],
    python_requires='>=3',
    include_package_data=True,    # muy importante para que se incluyan archivos sin extension .py
    version = '2.0.3',
    description ="pythonforchange.github.io",
    long_description=README1,
    long_description_content_type='text/markdown',
    author = 'Python For Change',
    author_email = 'pythonforchange@gmail.com',
    license="MIT",
    url = 'https://github.com/PythonForChange/pyforchange', # use the URL to the github repo
    download_url = 'https://github.com/PythonForChange/pyforchange/archive/refs/tags/v2.1.0.tar.gz',
    keywords = ['quantum','natural quantum script','nqs','pyforchange','console','covid', 'qiskit', 'language', 'plot', 'files'],
    classifiers = ['Programming Language :: Python :: 3','Intended Audience :: Developers','License :: OSI Approved :: MIT License','Natural Language :: English','Operating System :: OS Independent','Topic :: Text Processing :: Markup'],
    )