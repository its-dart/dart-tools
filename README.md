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


## Usage

### As a CLI

In the terminal, see the help message with
```bash
dart --help
```

Create a task with
```bash
dart createtask "new task"
```

Begin work on a task with
```bash
dart begintask
```

### As a Python Library

In Python, run
```python
from dart import login, create_task, begin_task

# only needed one time
login()

create_task("new task")

begin_task()
```

## Help and Resources

- [Homepage](https://www.itsdart.com/?nr=1)
- [Web App](https://app.itsdart.com/)
- [Help Center](https://its-dart.notion.site/Dart-Help-Center-8206a2aa2956496f8988b7b32cdcd205)
- [Bugs and Features](https://github.com/its-dart/dart-tools/issues)
- [Library Source](https://github.com/its-dart/dart-tools/)
- Email us at [support@itsdart.com](mailto:support@itsdart.com)
