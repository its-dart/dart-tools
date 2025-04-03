# Generate OpenAPI client.
api:
	admin/make-api.sh
	$(MAKE) blacken

# Run black on python files to format them.
blacken:
	uv run black ./dart ./examples

# Build a Python package and upload it to PyPI.
deploy:
	admin/make-deploy.sh
