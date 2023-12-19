#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import json

from dart import is_signature_correct, Task


# Adjust these depending on the situation within Dart
STANDARD_TITLE = "Approve to continue"
APPROVED_STATUS_DUID = "ryeJvn8mkhQS"  # This is the ID of the 'Approved' status; can be found by running this code and logging the `task.status_duid` when the task is moved to the 'Approved' status


def run_webhook(payload: bytes, headers: dict) -> bool:
    # Parse the event
    try:
        event = json.loads(payload)
    except TypeError as ex:
        print(f"Webhook error while parsing event: {ex}")
        return False

    # Verify the signature of the event
    signature = headers.get("Dart-Signature")
    if not is_signature_correct(payload, signature):
        print("Webhook signature verification failed")
        return False

    # Ignore if it wasn't an update
    event_type = event["type"]
    if event_type != "task.updated":
        return True

    # Ignore if it isn't relevant based on our criteria
    task = Task.from_dict(event["data"])
    if task.title != STANDARD_TITLE or task.status_duid != APPROVED_STATUS_DUID:
        return True

    # At this point we know that this is a relevant event, so we can do whatever we want with it
    print(f"Task {task.duid} was approved")

    return True
