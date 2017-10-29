#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""Download and init the external pkg"""

from os.path import exists

from core.settings.constants import PKG_DIRECTORY
from . import download_external_pkg


def initialize(force_init=False):
    """If the pkg folder not exist it download the new one but if if force_init it always download and init
     the external package.
     """
    if force_init or not exists(PKG_DIRECTORY):
        download_external_pkg.download_external_pkg.initialize(delete_old_pkg=True)
