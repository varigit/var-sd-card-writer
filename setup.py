# Copyright 2022 Variscite LTD
# SPDX-License-Identifier: BSD-3-Clause

import os
from setuptools import setup, find_packages
import re
import sys

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

PKG = "writer"
VERSION_FILE = os.path.join(PKG, "_version.py")
version = "unknown"
try:
    verstrline = open(VERSION_FILE, "rt").read()
except EnvironmentError:
    pass
else:
    VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
    mo = re.search(VSRE, verstrline, re.M)
    if mo:
        version = mo.group(1)
    else:
        sys.exit(f"Unable to find version in {VERSION_FILE}")

setup(
    name = "varwriter",
    version = version,
    author = "Alifer Moraes, Diego Dorta",
    description = "Variscite SD Card Writer Tool",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license = "BSD-3-Clause",
    url = "https://github.com/varigit/var-sd-card-writer",
    packages=find_packages(),
    entry_points = {
        'console_scripts' : ['varwriter = writer.varwriter:main']
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Information Technology',
        'Natural Language :: English',
        'Operating System :: Other OS',
        'Programming Language :: Python :: 3.7'
    ],
)
