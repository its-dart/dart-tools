#!/usr/bin/env bash
# -*- coding: utf-8 -*-

set -e

rm -rf dart/generated
uv run openapi-python-client generate --url https://app.itsdart.com/api/v0/public/schema/ --overwrite
mv dart-public-api-client/dart_public_api_client dart/generated
rm -rf dart-public-api-client

# Optimize API import paths
cat <<EOF >> dart/generated/api/__init__.py
from .comment import create_comment
from .config import get_config
from .dartboard import retrieve_dartboard
from .doc import (
    create_doc,
    delete_doc,
    list_docs,
    retrieve_doc,
    update_doc,
)
from .folder import retrieve_folder
from .task import (
    create_task,
    delete_task,
    list_tasks,
    retrieve_task,
    update_task,
)
from .view import retrieve_view
EOF
