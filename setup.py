# -*- coding: utf-8 -*-
#
# spikeplot - setup.py
#
# Philipp Meier <pmeier82 at googlemail dot com>
# 2011-09-30
#

"""install script for the SpikeEval package"""
__docformat__ = 'restructuredtext'

from setuptools import setup, find_packages

def find_version():
    """read version from __init__"""
    rval = '?'
    with open('./spikeplot/__init__.py', 'r') as f:
        for line in f:
            if line.startswith('__version__'):
                rval = line.split()[-1][1:-1]
                break
    return rval

DESC_TITLE = "SpikePlot : plotting package for spike sorting applications"
DESC_LONG = ''.join([DESC_TITLE, '\n\n', open('README', 'r').read()])
VERSION = find_version()

#print find_packages()

if __name__ == "__main__":
    setup(name="spikeplot",
          version=VERSION,
          packages=find_packages(),
          include_package_data=True,
          install_requires=[
              'scipy>=0.7.0',
              'matplotlib>=0.99.3'
          ],
          requires=[],

          # metadata
          author="Philipp Meier",
          author_email="pmeier82@googlemail.com",
          maintainer="Philipp Meier",
          maintainer_email="pmeier82@googlemail.com",
          description=DESC_TITLE,
          long_description=DESC_LONG,
          license="MIT License",
          url='http://ni.tu-berlin.de',
          classifiers=[
              'Development Status :: 4 - Beta',
              'Intended Audience :: Science/Research',
              'License :: OSI Approved :: MIT License',
              'Natural Language :: English',
              'Operating System :: OS Independent',
              'Programming Language :: Python',
              'Topic :: Scientific/Engineering :: Bio-Informatics'
          ])
