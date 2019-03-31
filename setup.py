#!/usr/bin/env python
import os
import sys
from setuptools import setup

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(__file__))
from pycnic import __version__

setup(
    name='pycnic',
    version=__version__,
    description='A simple, ultra light-weight, pure-python RESTful JSON API framework.',
    long_description=(
        'Pycnic offers a fully WSGI compliant JSON only web framework for '
        'quickly creating fast, modern web applications '
        'based on AJAX. Static files are served over a CDN or '
        'with a standard webserver, like Apache.'),
    author='Aaron Meier',
    author_email='webgovernor@gmail.com',
    maintainer='Dmitriy Geels',
    maintainer_email='dmitriy.geels@gmail.com',
    project_urls={
        'Source': 'https://github.com/dmig/pycnic',
        'Documentation': 'http://pycnic.nullism.com'
    },
    packages=['pycnic'],
    package_dir={'pycnic':'pycnic'},
    license='MIT',
    url='https://github.com/dmig/pycnic',
    install_requires=[],
    extras_require={'json': 'ujson'},
    provides=['pycnic'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Server',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ]
)
