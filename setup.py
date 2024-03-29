#!/usr/bin/env python
# coding: utf-8

"""
python-can requires the setuptools package to be installed.
"""

from __future__ import absolute_import

from os import listdir
from os.path import isfile, join
import re
import logging
from setuptools import setup, find_packages

logging.basicConfig(level=logging.WARNING)

with open('can/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

with open('README.rst', 'r') as f:
    long_description = f.read()

# Dependencies
extras_require = {
    'serial':   ['pyserial~=3.0'],
    'neovi':    ['python-ics>=2.12']
}

tests_require = [
    'mock~=2.0',
    'nose~=1.3',
    'pytest~=3.6',
    'pytest-timeout~=1.2',
    'pytest-cov~=2.5',
    'codecov~=2.0',
    'future',
    'six'
] + extras_require['serial']

extras_require['test'] = tests_require


setup(
    # Description
    name="python-can",
    url="https://github.com/hardbyte/python-can",
    description="Controller Area Network interface module for Python",
    long_description=long_description,
    classifiers=(
        # a list of all available ones: https://pypi.org/classifiers/
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Telecommunications Industry",
        "Natural Language :: English",
        "Topic :: System :: Logging",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Networking",
        "Topic :: System :: Hardware :: Hardware Drivers",
        "Topic :: Utilities"
    ),

    # Code
    version=version,
    packages=find_packages(exclude=["test", "test.*"]),
    scripts=list(filter(isfile, (join("scripts/", f) for f in listdir("scripts/")))),

    # Author
    author="Brian Thorne",
    author_email="brian@thorne.link",

    # License
    license="LGPL v3",

    # Package data
    package_data={
        "": ["CONTRIBUTORS.txt", "LICENSE.txt", "CHANGELOG.txt"],
        "doc": ["*.*"]
    },

    # Installation
    # see https://www.python.org/dev/peps/pep-0345/#version-specifiers
    python_requires=">=2.7,!=3.0,!=3.1,!=3.2,!=3.3",
    install_requires=[
        'wrapt~=1.10',
        'typing',
        'windows-curses;platform_system=="Windows"',
    ],
    extras_require=extras_require,

    # Testing
    test_suite="nose.collector",
    tests_require=tests_require,
)
