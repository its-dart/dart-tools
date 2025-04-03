#!/usr/bin/env bash
# -*- coding: utf-8 -*-

set -e

rm -rf dart/generated
uv run openapi-python-client generate --url https://app.itsdart.com/api/v0/public/schema/
mv dart-public-api-client/dart_public_api_client dart/generated
rm -rf dart-public-api-client
