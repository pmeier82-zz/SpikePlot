# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

DESC ="SpikePlot : plotting functions for spike sorting"
print find_packages()


if __name__ == "__main__":

    setup(name="neo",
          version='0.1.0',
          packages=find_packages(),
          include_package_data=True,
          install_requires=['scipy>=0.7.0', 'matplotlib>=0.99.3'],
          requires=[],

          # metadata for upload to PyPI
          author="Philipp Meier",
          author_email="pmeier82@googlemail.com",
          description=DESC,
          long_description=DESC,
          license="BSD",
          url='http://ni.tu-berlin.de',
          classifiers=['Development Status :: 3 - Alpha',
                       'Intended Audience :: Science/Research',
                       'License :: OSI Approved :: BSD License',
                       'Natural Language :: English',
                       'Operating System :: OS Independent',
                       'Programming Language :: Python',
                       'Topic :: Scientific/Engineering :: Bio-Informatics']
    )
