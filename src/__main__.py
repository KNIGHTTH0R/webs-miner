#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Main/Initial script for extract the data from the web sites.
"""

from core.init import init_pkg

init_pkg.initialize(force_init=True)

# noinspection PyPep8
import pkg
# noinspection PyPep8
from core.setup.get_web_links import get_web_links

# TODO: 1. Create test files for the current modules.
# TODO: 2. Move the pkg module into core, change in git ignore.
# TODO: 3. Move get_web_links into core, This file should be contains init_pkg.initialize(...) and init.start.
if __name__ == "__main__":
    get_web_links()
    print("get_open: ", pkg.html.tag.regex.get_open.get_open())
