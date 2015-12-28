from __future__ import unicode_literals

import re

from setuptools import find_packages, setup


def get_version(filename):
    with open(filename) as fh:
        metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", fh.read()))
        return metadata['version']


setup(
    name='Mopidy-SiriusXM',
    version=get_version('mopidy_siriusxm/__init__.py'),
    url='https://github.com/kdbdallas/mopidy-siriusxm',
    license='Apache License, Version 2.0',
    author='Dallas Brown',
    author_email='dbrown@port21.com',
    description='Mopidy extension for listening to Sirius XM Internet Radio (an active Sirius XM internet radio subscription is required)',
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=['tests', 'tests.*']),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'setuptools',
        'Mopidy >= 1.0',
        'Pykka >= 1.1',
        'pysiriusxm >= 0.1.0',
    ],
    entry_points={
        'mopidy.ext': [
            'siriusxm = mopidy_siriusxm:Extension',
        ],
    },
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Multimedia :: Sound/Audio :: Players',
    ],
)
