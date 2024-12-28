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


- [Setup](#setup)
- [Using the CLI](#using-the-cli)
- [Using the Python Library](#using-the-python-library)
- [Using the Python Library in AWS Lambda Functions](#using-the-python-library-in-aws-lambda-functions)
- [Advanced Usage](#advanced-usage)
- [Help and Resources](#help-and-resources)


## Setup

In the terminal, install by running
```bash
pip install dart-tools
```


## Using the CLI

Start off by setting up authentication with
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

First, set up authentication. Run `dart login` in the terminal for an interactive process, or visit [your Dart profile](https://app.itsdart.com/?settings=account) and then run `dart.login(token)` or save the token into the `DART_TOKEN` environment variable.

Then, you can run something like
```python
import os
from dart import create_task, is_logged_in, update_task

# Check that auth is set up and stop if not, can remove this once everything is set up
is_logged_in(should_raise=True)

# Create a new task called 'Update the landing page'
# With priority 'Critical' (i.e. p0) and with the 'marketing' tag
new_task = create_task(
    "Update the landing page", priority_int=0, tag_titles=["marketing"]
)

# Update the task to be 'Done'
update_task(new_task.duid, status_title="Done")
```

## Using the Python Library in AWS Lambda Functions

To use the `dart-tools` Python library in an AWS Lambda function, you need to package the library with your Lambda deployment package (see more details at [Working with .zip file archives for Python Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html)). Follow these steps:

1. Navigate to the directory containing your `lambda_function.py` source file. In this example, the directory is named `my_function`.

  ```bash
  cd my_function
  ```

2. Create a Deployment Package

  Use Docker to create a deployment package that includes the `dart-tools` library. Run the following commands in your terminal, ensuring that the `RUNTIME_PYTHON_VERSION` and `RUNTIME_ARCHITECTURE` environment variables match the runtime settings of your Lambda function:

  ```bash
  export RUNTIME_PYTHON_VERSION=3.12
  export RUNTIME_ARCHITECTURE=x86_64
  docker run --rm --volume ${PWD}:/app --entrypoint /bin/bash public.ecr.aws/lambda/python:${RUNTIME_PYTHON_VERSION}-${RUNTIME_ARCHITECTURE} -c "pip install --target /app/package dart-tools"
  ```

  This command installs the `dart-tools` library into a directory named `package` in your current working directory.

3. Zip the contents of the `package` directory along with your `lambda_function.py`

  ```bash
  cd package
  zip -r ../my_deployment_package.zip .
  cd ..
  zip -r my_deployment_package.zip lambda_function.py
  ```

4. Deploy the Lambda function

  Upload the `my_deployment_package.zip` file to AWS Lambda using the AWS Management Console or the AWS CLI.

By following these steps, you can use the `dart-tools` Python library within your AWS Lambda functions.

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

# Initialize the inner client
dart = Dart()

# Prepare the update operation
task_update = TaskUpdate(
    duid="[DUID]",
    size=5,
)
task_update_op = Operation(
    model=OperationModelKind.TASK,
    kind=OperationKind.UPDATE,
    data=task_update,
)

# Call the operation transactionally to perform the update
response = dart.transact([task_update_op], TransactionKind.TASK_UPDATE)
```


## Help and Resources

- [Homepage](https://www.itsdart.com/?nr=1)
- [Web App](https://app.itsdart.com/)
- [Help Center](https://help.itsdart.com/)
- [Bugs and Features](https://github.com/its-dart/dart-tools/issues)
- [Library Source](https://github.com/its-dart/dart-tools/)
- [Chat on Discord](https://discord.gg/RExv8jEkSh)
- Email us at [support@itsdart.com](mailto:support@itsdart.com)
