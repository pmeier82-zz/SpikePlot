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

DESC_TITLE = "SpikePlot : plotting package for spike sorting applications"
DESC_LONG = ''.join([DESC_TITLE, '\n\n', open('README', 'r').read()])

#print find_packages()

if __name__ == "__main__":
    setup(name="spikeplot",
          version='0.1.1',
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
