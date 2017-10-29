#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Contain the constants for this app.
"""

from os.path import abspath, dirname, join, realpath

_constant_file_path = dirname(realpath(__file__))

SRC_DIRECTORY = abspath(join(_constant_file_path, '../../')) + '/'
