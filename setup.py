#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
from setuptools import setup

with io.open('README.rst', encoding='utf-8') as readme:
    description = readme.read()

setup(
  name='django-settings-local',
  packages=['django_settings_local'],
  version='0.1.5',
  description='Manage Django Local Settings',
  long_description=description,
  author='Fasih Ahmad Fakhri',
  author_email='fasih@email.com',
  url='https://github.com/fasih/django-settings-local',
  download_url='https://github.com/fasih/django-settings-local/archive/0.1.5.tar.gz',
  keywords='django local settings',
  entry_points={
    'console_scripts': [
      'dsl = django_settings_local.__main__:main',
    ],
  },
  license='GPL-3.0',
  classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Framework :: Django',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries'
    ],
    python_requires='>=3.6',
)
