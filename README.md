# dart-tools

[Dart](https://itsdart.com?nr=1) is Project Management on Autopilot.

This is the Dart CLI and Python Library. It enables direct interation with Dart through a terminal CLI or through Python.


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
