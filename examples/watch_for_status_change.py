#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import json

from dart import is_signature_correct


# Adjust these depending on the situation within Dart
STANDARD_TITLE = "Approve to continue"
APPROVED_STATUS = "Approved"


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
    task = event["data"]
    if task["title"] != STANDARD_TITLE or task.status != APPROVED_STATUS:
        return True

    # At this point we know that this is a relevant event, so we can do whatever we want with it
    print(f"Task {task.ID} was approved")

    return True
