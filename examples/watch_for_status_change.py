#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import json

from dart import is_signature_correct, Task


# Easiest way to get this is to watch an event come in for the status in question and see what its ID is from that
STANDARD_TITLE = "Approve to continue"
APPROVED_STATUS_ID = "o8MW4doZyIqm"


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

    # Ignore if it didn't change to the status we're looking for
    task = Task.from_dict(event["data"])
    if task.title != STANDARD_TITLE or task.status_duid != APPROVED_STATUS_ID:
        return True

    # At this point we know that this is a relevant event, so we can do whatever we want with it
    print(f"Task {task.duid} was approved")

    return True
