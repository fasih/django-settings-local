#!/usr/bin/env python
# -*- coding: utf-8 -*-

import django_settings_local
from setuptools import setup

VERSION = django_settings_local.__version__

setup(
  download_url=f'https://github.com/fasih/django-settings-local/archive/{VERSION}.tar.gz',
)
