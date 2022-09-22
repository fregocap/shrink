import os

import pkg_resources
from setuptools import setup, find_packages 

setup(
    name="shrink",
    py_modules=["shrink"],
    version="0.0.1",
    description="",
    author="Fabio Capela",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__),"requirements.txt"))
        )
    ],
    entry_points={},
    include_package_data=True,
    extras_require={'dev':['pytest']}
)