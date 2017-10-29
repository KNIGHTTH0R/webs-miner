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

from core.settings.constants import PKG_DIRECTORY, PKG_FILE, SRC_DIRECTORY

# TODO: Crete test for this file.
_pkg_url = 'https://raw.githubusercontent.com/airvzxf/python-packages/master/versions/pkg_last_version.tar.gz'


def _delete_pkg_folder():
    if exists(PKG_DIRECTORY) and isdir(PKG_DIRECTORY):
        shutil.rmtree(PKG_DIRECTORY)


def _delete_pkg_file():
    if exists(PKG_FILE):
        remove(PKG_FILE)


def _download_pkg_file():
    _delete_pkg_file()
    urlretrieve(_pkg_url, PKG_FILE)


def _download_pkg_modules():
    if not exists(PKG_FILE):
        _download_pkg_file()
        return True

    response = requests.head(_pkg_url)
    file_size = int(response.headers.get('Content-Length'))

    with open(PKG_FILE, 'rb') as local_file:
        if file_size != len(local_file.read()):
            _download_pkg_file()
            return True

    return False


def _extract_pkg_modules():
    with tarfile.open(PKG_FILE, 'r:gz') as tar_gz_file:
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
