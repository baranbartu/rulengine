#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages
from rulengine import __version__

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

packages = find_packages()

setup(
    name='rulengine',
    version=__version__,
    description='Simple Rule Engine',
    long_description=README,
    url='https://github.com/baranbartu/rulengine',
    download_url='https://github.com/baranbartu/rulengine/tarball/%s' % (
        __version__,),
    author='Baran Bartu Demirci',
    author_email='bbartu.demirci@gmail.com',
    license='MIT',
    keywords='python,rule,rule executor,rule engine',
    packages=packages
)
