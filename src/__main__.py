#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""Main/Initial script for extract the data from the web sites."""

import yaml

from init import init_pkg

init_pkg.initialize()

# noinspection PyPep8
import pkg

if __name__ == "__main__":
    # Config files:
    # https://martin-thoma.com/configuration-files-in-python/
    # https://stackoverflow.com/questions/6866600/yaml-parsing-and-python
    # YAML is better for config files vs JSON.
    print("get_open: ", pkg.html.tag.regex.get_open.get_open())
    with open('./config/web_links.yaml') as yaml_file:
        web_links_list_config = yaml.load(yaml_file)

    for web_page in web_links_list_config:
        print(web_page)
