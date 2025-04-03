#!/usr/bin/env bash
# -*- coding: utf-8 -*-

set -e

rm -rf dart/generated
uv run openapi-python-client generate --url https://app.itsdart.com/api/v0/public/schema/
mv dart-api-client/dart_api_client dart/generated
rm -rf dart-api-client
