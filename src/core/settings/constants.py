#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Contain the constants for this app.
"""

from os.path import abspath, dirname, join, realpath

_constant_file_path = dirname(realpath(__file__))

SRC_DIRECTORY = abspath(join(_constant_file_path, '../../')) + '/'

PKG_DIRECTORY = SRC_DIRECTORY + 'pkg/'
PKG_FILE = SRC_DIRECTORY + 'pkg_last_version.tar.gz'
PKG_URL = 'https://raw.githubusercontent.com/airvzxf/python-packages/master/versions/pkg_last_version.tar.gz'
