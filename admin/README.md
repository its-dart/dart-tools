# Admin functionality

## Local setup

1. Install with `pip install .`


## Sync API

1. Run `admin/make-openapi.sh`


## Deploy setup

1. Run `pip install build twine` as needed
1. Get an existing PyPI token or [make a new one](https://pypi.org/manage/account/token/)
1. Fill out `~/.pypirc` according to [the specification](https://packaging.python.org/en/latest/specifications/pypirc/#using-a-pypi-token)


## Deploy

1. Bump the version in `pyproject.toml`
1. Run `admin/make-deploy.sh`
