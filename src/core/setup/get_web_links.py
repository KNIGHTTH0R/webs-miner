#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Extract the web links into the preferences file and return a list.
"""

import yaml

# TODO: Crete test for this file.
from core.settings.constants import PREFERENCES_WEB_LINKS


def get_web_links():
    """
    Get the web links from the yaml preferences file.
    """
    with open(PREFERENCES_WEB_LINKS) as yaml_file:
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
