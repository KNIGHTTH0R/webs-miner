#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""Main/Initial script for extract the data from the web sites."""

import init_pkg

init_pkg.initialize()

# noinspection PyPep8
import pkg

if __name__ == "__main__":
    # Config files:
    # https://martin-thoma.com/configuration-files-in-python/
    # https://stackoverflow.com/questions/6866600/yaml-parsing-and-python
    # YAML is better for config files vs JSON.
    print("get_open: ", pkg.html.tag.regex.get_open.get_open())
    pass

# First I need a list with this data.
# ----------------------------------------------------------------------
# Link: https://www.bose.com/en_us/products/headphones/over_ear_headphones/quietcomfort-35-wireless-ii.html
# Brand: BOSE
# Model: Quiet comfort 35 Wireless II / Black
# SKU: 789564
# Category: Headphones
# Sub-category: Wireless
# ----------------------------------------------------------------------
# Link: http://store.asus.com/us/item/201702AM030000001
# Brand: ASUS
# Model: ROG G701VI-XS72K OC Edition
# SKU: 201702AM030000001
# Category: Laptop
# Sub-category: None
# ----------------------------------------------------------------------
# Link: https://store.asus.com/us/item/201701AM100000021
# Brand: ASUS
# Model: ROG Ranger Backpack
# SKU: 201701AM100000021
# Category: Laptop
# Sub-category: Backpack
# ----------------------------------------------------------------------
