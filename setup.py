# -*- coding: utf-8 -*-
#
# spikeplot - setup.py
#
# Philipp Meier <pmeier82 at googlemail dot com>
# 2011-09-30
#

"""install script for the SpikeEval package"""
__author__ = 'Philipp Meier <pmeier82 at googlemail dot com>'
__docformat__ = 'restructuredtext'

from setuptools import setup, find_packages

DESC_TITLE = "SpikePlot : plotting package for spike sorting applications"
DESC_LONG = ''.join([DESC_TITLE, '\n\n', open('README', 'r').read()])

#print find_packages()

if __name__ == "__main__":
    setup(name="spikeplot",
          version='0.1.0',
          packages=find_packages(),
          include_package_data=True,
          install_requires=['scipy>=0.7.0', 'matplotlib>=0.99.3'],
          requires=[],

          # metadata for upload to PyPI
          author="Philipp Meier",
          author_email="pmeier82@googlemail.com",
          maintainer="Philipp Meier",
          maintainer_email="pmeier82@googlemail.com",
          description=DESC_TITLE,
          long_description=DESC_LONG,
          license="EUPL v1.1",
          url='http://ni.tu-berlin.de',
          classifiers=['Development Status :: 3 - Alpha',
                       'Intended Audience :: Science/Research',
                       'License :: OSI Approved :: BSD License',
                       'Natural Language :: English',
                       'Operating System :: OS Independent',
                       'Programming Language :: Python',
                       'Topic :: Scientific/Engineering :: Bio-Informatics'])
