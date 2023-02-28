#!/usr/bin/env bash
# -*- coding: utf-8 -*-

set -e

python3 -m build --sdist .

twine upload dist/*
