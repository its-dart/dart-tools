# Admin functionality

- [Admin functionality](#admin-functionality)
  - [Install local version](#install-local-version)
  - [Test with a different Python version](#test-with-a-different-python-version)
  - [Sync API](#sync-api)
  - [Deploy setup](#deploy-setup)
  - [Deploy](#deploy)

## Install local version

1. Run `uv sync` as needed
2. Install with `uv pip install .`

## Test with a different Python version

1. Choose the version with `uv venv --python 3.x`
2. Run `uv sync`

## Sync API

1. Run `uv sync` as needed
2. Run `make api`

## Deploy setup

1. Run `uv sync` as needed
2. Get an existing PyPI token or [make a new one](https://pypi.org/manage/account/token/)
3. Set the `UV_PUBLISH_TOKEN` environment variable, for example, by running `export UV_PUBLISH_TOKEN=<PyPI token>`

## Deploy

1. Bump the version in `pyproject.toml`
2. Run `uv sync`
3. Run `make deploy`
4. Commit and push all local changes to GitHub
