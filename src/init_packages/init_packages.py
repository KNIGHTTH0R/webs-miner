#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""Extract information from a web page and save in a database then you can visualized in a char.
Download the last version of the pkg modules which is my personal library.
https://raw.githubusercontent.com/airvzxf/python-packages/master/versions/pkg_last_version.tar.gz
"""

import shutil
import tarfile
from os.path import dirname, exists, isdir, realpath
# noinspection PyCompatibility
from urllib.request import urlretrieve

import requests

_src_directory = dirname(realpath(__file__)) + '/../'
_pkg_directory = _src_directory + 'pkg/'
_pkg_file_name = 'pkg_last_version.tar.gz'
_pkg_url = 'https://raw.githubusercontent.com/airvzxf/python-packages/master/versions/' + _pkg_file_name


def _download_pkg_file():
    urlretrieve(_pkg_url, _src_directory + _pkg_file_name)


def _download_pkg_modules():
    if not exists(_src_directory + _pkg_file_name):
        _download_pkg_file()
        return True

    response = requests.head(_pkg_url)
    file_size = int(response.headers.get('Content-Length'))

    with open(_src_directory + _pkg_file_name, 'rb') as local_file:
        if file_size != len(local_file.read()):
            _download_pkg_file()
            return True

    return False


def _delete_pkg_file_and_folder():
    if exists(_pkg_directory) and isdir(_pkg_directory):
        shutil.rmtree(_pkg_directory)


def _extract_pkg_modules():
    _delete_pkg_file_and_folder()

    with tarfile.open(_src_directory + _pkg_file_name, 'r:gz') as tar_gz_file:
        tar_gz_file.extractall(_src_directory)


def initialize(delete_pkg=True):
    """Init the process to check the external packages.
    Check if the external packages exist otherwise it remove the old then download and extract the new packages.
    """

    if delete_pkg:
        _delete_pkg_file_and_folder()

    if _download_pkg_modules():
        print("Download {}".format(_pkg_file_name))
        _extract_pkg_modules()
        print("Extracted packages.")
