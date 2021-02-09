#!/usr/bin/env python
"""
astrojobs: Get latest astronomy job and rumor news in your command line

Project website: https://github.com/pmocz/astrojobs

The MIT License (MIT)
Copyright (c) 2021 Philip Mocz (pmocz)
http://opensource.org/licenses/MIT
"""
from __future__ import absolute_import

import os

from setuptools import setup

_name = "astrojobs"
_version = ""
with open(os.path.join(os.path.dirname(__file__), "{}.py".format(_name))) as _f:
    for _l in _f:
        if _l.startswith("__version__ = "):
            _version = _l.partition("=")[2].strip().strip("'").strip('"')
            break
if not _version:
    raise ValueError("__version__ not define!")

setup(
    name=_name,
    version=_version,
    description="Find all citation keys in your LaTeX documents and search NASA ADS to generate corresponding bibtex entries.",
    url="https://github.com/pmocz/{}".format(_name),
    download_url="https://github.com/pmocz/{}/archive/v{}.tar.gz".format(
        _name, _version
    ),
    author="Philip Mocz",
    author_email="philip.mocz@gmail.com",
    maintainer="Philip Mocz",
    maintainer_email="philip.mocz@gmail.com",
    license="MIT",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering :: Astronomy",
    ],
    keywords="astronomy job rumor",
    py_modules=[_name],
    install_requires=[
        "bs4>=0.0.1",
        "urllib>=1.25.7",
        "requests>=2.0",
        "wasabi>=0.8.2",
        "future>=0.12.0 ; python_version < '3.0'",
    ],
    entry_points={"console_scripts": ["astrojobs=astrojobs:main"]},
)
