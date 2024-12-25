# Admin functionality


- [Admin functionality](#admin-functionality)
  - [Local setup](#local-setup)
  - [Sync API](#sync-api)
  - [Deploy setup](#deploy-setup)
  - [Deploy](#deploy)


## Local setup

1. Install with `pip install .`


## Sync API

1. Run `pip install openapi-python-client` as needed
2. Run `admin/make-api.sh`


## Deploy setup

1. Run `pip install build twine` as needed
2. Get an existing PyPI token or [make a new one](https://pypi.org/manage/account/token/)
3. Fill out `~/.pypirc` according to [the specification](https://packaging.python.org/en/latest/specifications/pypirc/#using-a-pypi-token)


## Deploy

1. Bump the version in `pyproject.toml`
2. Run `admin/make-deploy.sh`
