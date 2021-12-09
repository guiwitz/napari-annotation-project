#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


# https://github.com/pypa/setuptools_scm
use_scm = {"write_to": "src/napari_annotation_project/_version.py"}
setup(use_scm_version=use_scm)
