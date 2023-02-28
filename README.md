# dart-tools

The Dart CLI and Python Library


## Introduction

[Dart] is Project Management on Autopilot.

This module enables direct interation with Dart through a terminal CLI or through Python.


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
