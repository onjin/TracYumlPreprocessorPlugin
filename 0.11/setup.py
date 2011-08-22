#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name = 'YumlPreprocessor',
    version = '0.1',
    packages = ['yumlpreprocessor'],

    author = "dthomas",
    description = "A preprocessor for including UML diagrams using the http://yuml.me service. ",
    license = "GPL",
    keywords = "trac yuml preprocessor macro plugin",
    url = "http://trac-hacks.org/wiki/YumlPreprocessorMacro",
    classifiers = [
        'Framework :: Trac',
    ],
    

    entry_points = {
        'trac.plugins': [
            'yumlpreprocessor.YumlPreprocessor = yumlpreprocessor.YumlPreprocessor',
        ]
    }
)
