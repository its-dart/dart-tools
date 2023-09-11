#!/usr/bin/env bash
# -*- coding: utf-8 -*-

set -e

rm -rf generated
openapi-python-client generate --url https://app.itsdart.com/api/v0/schema/
mv dart-api-client/dart_api_client generated
rm -rf dart-api-client
