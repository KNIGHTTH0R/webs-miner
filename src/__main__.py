#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Extract information from a web page and save in a database then you can visualized in a char.
Download the last version of the pkg modules which is my personal library.
https://raw.githubusercontent.com/airvzxf/python-packages/master/versions/pkg_last_version.tar.gz
"""

import shutil
import tarfile
from os.path import dirname, realpath, exists, isdir
# noinspection PyCompatibility
from urllib.request import urlretrieve

import requests

current_directory = dirname(realpath(__file__)) + '/'
pkg_directory = current_directory + 'pkg/'
pkg_file_name = 'pkg_last_version.tar.gz'
pkg_url = 'https://raw.githubusercontent.com/airvzxf/python-packages/master/versions/' + pkg_file_name


def _download_pkg_file():
    urlretrieve(pkg_url, pkg_file_name)

    pass


def _download_pkg_modules():
    if not exists(pkg_file_name):
        _download_pkg_file()
        return True

    response = requests.head(pkg_url)
    file_size = int(response.headers.get('Content-Length'))

    with open(pkg_file_name, 'rb') as local_file:
        if file_size != len(local_file.read()):
            _download_pkg_file()
            return True

    return False


def _extract_pkg_modules():
    if exists(pkg_directory) and isdir(pkg_directory):
        shutil.rmtree(pkg_directory)

    with tarfile.open(pkg_file_name, 'r:gz') as tar_gz_file:
        tar_gz_file.extractall('.')

    pass


if __name__ == "__main__":
    if _download_pkg_modules():
        _extract_pkg_modules()

    pass
