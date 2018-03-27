#!/usr/bin/env python

from setuptools import setup

version = "0.19"

setup(
    name="pycoinnet",
    version=version,
    packages=[
        "pycoinnet",
        "pycoinnet.cmds",
    ],
    entry_points={'console_scripts': [
        'blockwatcher = pycoinnet.examples.blockwatcher:main',
    ]},
    author="Richard Kiss",
    author_email="him@richardkiss.com",
    url="https://github.com/richardkiss/pycoinnet",
    license="http://opensource.org/licenses/MIT",
    description="Network utilities for communicating on the bitcoin network.",
)
