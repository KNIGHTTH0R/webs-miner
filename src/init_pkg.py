#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""Download and init the external pkg"""

from os.path import dirname, exists, realpath

import init_packages


def initialize(force_init=False):
    """If the pkg folder not exist it download the new one but if if force_init it always download and init
     the external package.
     """
    _current_directory = dirname(realpath(__file__))

    if not exists(_current_directory + '/pkg/'):
        init_packages.init_packages.initialize(delete_pkg=True)

    if force_init:
        init_packages.init_packages.initialize(delete_pkg=True)
