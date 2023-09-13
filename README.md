<div align="center">
  <h1>Dart Tools</h1>
  <p>
    <a href="https://pypi.org/project/dart-tools"><img src="https://img.shields.io/pypi/v/dart-tools.svg" alt="PyPI"></a>
    <a href="tox.ini"><img src="https://img.shields.io/pypi/pyversions/dart-tools" alt="Supported Python Versions"></a>
    <a href="LICENSE"><img src="https://img.shields.io/github/license/its-dart/dart-tools" alt="License"></a>
  </p>
</div>

[Dart](https://itsdart.com?nr=1) is Project Management powered by AI.

`dart-tools` is the Dart CLI and Python Library. It enables direct integration with Dart through a terminal CLI or through Python.


## Setup

In the terminal, install by running
```bash
pip install dart-tools
```


## Using the CLI

As an example, start off by logging in with
```bash
dart login
```

Then, you can create a new task with a command along the lines of
```bash
dart createtask "Update the landing page" -p0 --tag marketing
```
which will make a new task called 'Update the landing page' with priority 'Critical' (i.e. P0) and with the 'marketing' tag.

You can explore all of these options and many more with `dart --help` or the more specific help for subcommands, in this case `dart createtask --help`.

Another common workflow is to updating a preexisting task. To do this, run something like
```bash
dart updatetask [DUID] -s Done
```
This command will mark the referenced task 'Done'. Here `[DUID]` is meant to be replaced (including the brackets) with the 'Dart ID' of an existing task. You can get a DUID from any existing task in a number of ways, such as by copying it from the end of a task's URL or by clicking the '...' button in a task page in Dart and then choosing 'Copy ID'.


## Using the Python Library

In Python, you can run something like
```python
import os
from dart import is_logged_in, login, create_task, update_task

# login based on information stored in environment variables, but only if needed
if not is_logged_in():
    login(email=os.environ["DART_EMAIL"], password=os.environ["DART_PASSWORD"])

# create a new task called 'Update the landing page'
# with priority 'Critical' (i.e. p0) and with the 'marketing' tag
new_task = create_task(
    "Update the landing page", priority_int=0, tag_titles=["marketing"]
)

# update the task to be 'Done'
update_task(new_task.duid, status_title="Done")
```


## Advanced Usage

Almost anything that can be done in Dart can be done with the Python library, but there are not convenient wrapper functions for everything.
For most advanced usage, the best thing to do is to [get in touch with us](mailto:support@itsdart.com) and we can help.

However, if you want to explore on your own, the client is well-typed, so you can simply explore the code to see what is possible.
All updates will go through the the `dart.transact` function.

As an example, you could run something akin to `update_task` with
```python
from dart import (
    Dart,
    Operation,
    OperationKind,
    OperationModelKind,
    TaskUpdate,
    TransactionKind,
)

# initialize the inner client
dart = Dart()

# prepare the update operation
task_update = TaskUpdate(
    duid="[DUID]",
    size=5,
)
task_update_op = Operation(
    model=OperationModelKind.TASK,
    kind=OperationKind.UPDATE,
    data=task_update,
)

# call the operation transactionally to preform the update
response = dart.transact([task_update_op], TransactionKind.TASK_UPDATE)
```


## Help and Resources

- [Homepage](https://www.itsdart.com/?nr=1)
- [Web App](https://app.itsdart.com/)
- [Help Center](https://its-dart.notion.site/Dart-Help-Center-8206a2aa2956496f8988b7b32cdcd205)
- [Bugs and Features](https://github.com/its-dart/dart-tools/issues)
- [Library Source](https://github.com/its-dart/dart-tools/)
- [Chat on Discord](https://discord.gg/RExv8jEkSh)
- Email us at [support@itsdart.com](mailto:support@itsdart.com)
