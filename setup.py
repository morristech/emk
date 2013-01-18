import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "emk",
    version = "0.0.1",
    author = "Ken MacKay",
    description = ("A fast cross-compiling build system, written in Python."),
    license = "BSD",
    keywords = "build compile make cross-compiler",
    url = "https://github.com/kmackay/emk",
    py_modules = ['emk'],
    package_dir = {'emk.modules': 'modules'},
    packages = ['emk.modules'],
    scripts = ['emk'],
    requires=['appdirs'],
    long_description = read('README.md'),
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: BSD License"
    ]
)
