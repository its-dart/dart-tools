<div align="center">
  <h1>Dart Tools</h1>
  <p>
    <a href="https://pypi.org/project/dart-tools"><img src="https://img.shields.io/pypi/v/dart-tools.svg" alt="PyPI"></a>
    <a href="tox.ini"><img src="https://img.shields.io/pypi/pyversions/dart-tools" alt="Supported Python Versions"></a>
    <a href="LICENSE"><img src="https://img.shields.io/github/license/its-dart/dart-tools" alt="License"></a>
  </p>
</div>

[Dart](https://itsdart.com?nr=1) is Project Management on Autopilot.

`dart-tools` is the Dart CLI and Python Library. It enables direct integration with Dart through a terminal CLI or through Python.


## Setup

In the terminal, install with
```bash
pip install dart-tools
```

Then, login with
```bash
dart login
```


## Using the CLI

As an example, start off by logging in with
```bash
dart login
```

Then, you can create a new task with
```bash
dart createtask "Update the landing page" -p0 --tag marketing
```
which will make a new task called 'Update the landing page' with priority 'Critical' (i.e. p0) and with the 'marketing' tag.
You can explore all of these options and many more with `dart --help` or, for example, `dart createtask --help`.

Another common workflow is to updating a preexisting task. To do this, run something like
```bash
dart updatetask DUID -s Done
```
where `DUID` is the ID of an existing task. This command will mark the referenced task 'Done'.


## Using the Python Library

In Python, run something like
```python
import os
from dart import is_logged_in, login, create_task, update_task

# login only if needed, based on information stored in environment variables
if not is_logged_in():
  login(email=os.environ["DART_EMAIL"], password=os.environ["DART_PASSWORD"])

# create a new task called 'Update the landing page' with priority 'Critical' (i.e. p0) and with the 'marketing' tag
new_task = create_task("Update the landing page", priority=0, tag_titles=["marketing"])

# update the task to be 'Done'
update_task(new_task.duid, status_title="Done")
```


## Help and Resources

- [Homepage](https://www.itsdart.com/?nr=1)
- [Web App](https://app.itsdart.com/)
- [Help Center](https://its-dart.notion.site/Dart-Help-Center-8206a2aa2956496f8988b7b32cdcd205)
- [Bugs and Features](https://github.com/its-dart/dart-tools/issues)
- [Library Source](https://github.com/its-dart/dart-tools/)
- Email us at [support@itsdart.com](mailto:support@itsdart.com)
