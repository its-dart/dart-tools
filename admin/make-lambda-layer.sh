#!/usr/bin/env bash
# -*- coding: utf-8 -*-

set -e

rm -rf layer.zip || true

cat << 'EOF' > Dockerfile
FROM public.ecr.aws/lambda/python:3.12
RUN dnf install -y gcc zip
WORKDIR /layer
RUN pip install dart-tools -t python/lib/python3.12/site-packages
RUN zip -r layer.zip python/
ENTRYPOINT []
CMD ["sleep", "1"]
EOF

docker build --no-cache --platform linux/amd64 -t layer-builder .
docker create --name layer layer-builder
docker cp layer:/layer/layer.zip ./layer.zip
docker rm layer

rm Dockerfile
