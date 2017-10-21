#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""Main/Initial script for extract the data from the web sites."""

import init_pkg

init_pkg.initialize()

# noinspection PyPep8
import pkg

if __name__ == "__main__":
    print("get_open: ", pkg.html.tag.regex.get_open.get_open())
    pass
