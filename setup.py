#!/usr/bin/env python
# setup.py
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import sys

# windows installer:
# python setup.py bdist_wininst

# patch distutils if it can't cope with the "classifiers" or
# "download_url" keywords
if sys.version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None

import os
if os.name == 'nt':
    # set dependencies for windows version
    data_files = {'parallel': ['simpleio.dll']}
else:
    # no dependencies
    data_files = {}


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='pyparallel',
    description='Python Parallel Port Extension',
    version='0.2.2',
    author='Chris Liechti',
    author_email='cliechti@gmx.net',
    url='https://github.com/pyserial/pyparallel',
    packages=['parallel'],
    license='BSD',
    long_description=read('README.rst'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Communications',
        'Topic :: Software Development :: Libraries',
    ],
    package_data=data_files
)
