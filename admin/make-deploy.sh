#!/usr/bin/env bash
# -*- coding: utf-8 -*-

set -e

rm -rf dist
python3 -m build .
twine upload dist/*
