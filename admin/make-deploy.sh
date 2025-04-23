#!/usr/bin/env bash
# -*- coding: utf-8 -*-

set -e

rm -rf dist
uv build
uv publish
