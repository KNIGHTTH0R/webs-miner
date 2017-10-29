#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""Extract information from a web page and save in a database then you can visualized in a char.
Download the last version of the pkg modules which is my personal library.
https://raw.githubusercontent.com/airvzxf/python-packages/master/versions/pkg_last_version.tar.gz
"""

import shutil
import tarfile
from os import remove
from os.path import exists, isdir
# noinspection PyCompatibility
from urllib.request import urlretrieve

import requests

from core.settings.constants import SRC_DIRECTORY

# TODO: Crete test for this file.
_pkg_file_name = SRC_DIRECTORY + 'pkg_last_version.tar.gz'
_pkg_url = 'https://raw.githubusercontent.com/airvzxf/python-packages/master/versions/pkg_last_version.tar.gz'


def _delete_pkg_folder():
    pkg_directory = SRC_DIRECTORY + 'pkg/'

    if exists(pkg_directory) and isdir(pkg_directory):
        shutil.rmtree(pkg_directory)


def _delete_pkg_file():
    if exists(_pkg_file_name):
        remove(_pkg_file_name)


def _download_pkg_file():
    _delete_pkg_file()
    urlretrieve(_pkg_url, _pkg_file_name)


def _download_pkg_modules():
    if not exists(_pkg_file_name):
        _download_pkg_file()
        return True

    response = requests.head(_pkg_url)
    file_size = int(response.headers.get('Content-Length'))

    with open(_pkg_file_name, 'rb') as local_file:
        if file_size != len(local_file.read()):
            _download_pkg_file()
            return True

    return False


def _extract_pkg_modules():
    with tarfile.open(_pkg_file_name, 'r:gz') as tar_gz_file:
        _delete_pkg_folder()
        tar_gz_file.extractall(SRC_DIRECTORY)


def initialize(delete_old_pkg=True):
    """Init the process to check the external packages.
    Check if the external packages exist otherwise it remove the old then download and extract the new packages.
    """

    if delete_old_pkg:
        _delete_pkg_file()

    if _download_pkg_modules():
        print("Download pkg file.")
        _extract_pkg_modules()
        print("Extracted packages.")
        print('')
