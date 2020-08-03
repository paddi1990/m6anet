"""Setup for the m6anet package."""

from setuptools import setup,find_packages

__pkg_name__ = 'm6anet'


with open('README.md') as f:
    README = f.read()

setup(
    author="Christopher Hendra",
    maintainer_email="christopher.hendra@u.nus.edu",
    name=__pkg_name__,
    license="MIT",
    description='m6anet is a python package for detection of m6a modifications from Nanopore direct RNA sequencing data.',
    version='v0.0.1',
    long_description=README,
    url='https://github.com/GoekeLab/m6anet',
    packages=find_packages(),
    python_requires=">=3.5",
    install_requires=[],
    entry_points={'console_scripts': ["m6anet-dataprep={}.scripts.dataprep:main".format(__pkg_name__),
                                      "m6anet-inference={}.scripts.inference:main".format(__pkg_name__)]},
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Intended Audience :: Science/Research',
    ],
)
