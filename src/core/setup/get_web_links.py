#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""Extract the web links into the preferences file and return a list."""

from os.path import dirname, realpath

import yaml


# TODO: Crete test for this file.
def get_web_links():
    """
    Get the web links from the yaml preferences file.
    """
    _current_directory = dirname(realpath(__file__))

    with open(_current_directory + '/../../preferences/web_links.yaml') as yaml_file:
        web_links_list_config = yaml.load(yaml_file)

        if not web_links_list_config:
            print('Error: web links preferences file is empty.')
            print('The file web_links.yaml in ./preferences folder is empty. You need to add your web links')
            exit(code=1)

        for web_page_key in web_links_list_config:
            print("web_page_key: ", web_page_key)
            web_page = web_links_list_config.get(web_page_key)
            print("link: ", web_page.get('link'))
            print("brand: ", web_page.get('brand'))
            print("model: ", web_page.get('model'))
            print("sku: ", web_page.get('sku'))
            print("category: ", web_page.get('category'))
            print("sub_category: ", web_page.get('sub_category'))
            print("")
