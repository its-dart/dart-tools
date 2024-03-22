#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# README: https://its-dart.notion.site/27064491a4694d0fb2b27d8294a6e3fa


import json

from dart import is_signature_correct, Task
from flask import Flask, Response, jsonify, request


app = Flask(__name__)


@app.route("/", methods=["POST"])
def webhook() -> Response:
    payload = request.data

    # Parse the event
    try:
        event = json.loads(payload)
    except TypeError as ex:
        print(f"Webhook error while parsing event: {ex}")
        return jsonify(success=False)

    # Verify the signature of the event
    signature = request.headers.get("Dart-Signature")
    if not is_signature_correct(payload, signature):
        print("Webhook signature verification failed")
        return jsonify(success=False)

    # Handle the event
    event_type = event["type"]
    match event_type:
        case "task.created":
            task = event["data"]["model"]  # The task that was created
            print(f"Task created:\n{Task.from_dict(task)}")
        case "task.updated":
            data = event["data"]
            task = data["model"]  # The new version of the task that was updated
            old_task = data["oldModel"]  # The old version of the task that was updated
            print(f"Task updated:\n{Task.from_dict(task)}")
        case "task.deleted":
            task = event["data"]["model"]  # The task that was deleted
            print(f"Task deleted:\n{Task.from_dict(task)}")
        case _:
            # Unexpected event type
            print(f"Unhandled event type: {event_type}")
            return jsonify(success=False)

    return jsonify(success=True)


if __name__ == "__main__":
    app.run(debug=True)
