#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# README: https://its-dart.notion.site/27064491a4694d0fb2b27d8294a6e3fa


import json

from dart import is_signature_correct
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
    if event_type == "task.created":
        task = event["data"]  # Contains details of the task that was created
        print(f"Task created:\n{json.dumps(task, indent=2)}")
    elif event_type == "task.updated":
        task = event["data"]  # Contains details of the task that was updated
        print(f"Task updated:\n{json.dumps(task, indent=2)}")
    elif event_type == "task.deleted":
        task = event["data"]  # Contains details of the task that was deleted
        print(f"Task deleted:\n{json.dumps(task, indent=2)}")
    else:
        # Unexpected event type
        print(f"Unhandled event type: {event_type}")
        return jsonify(success=False)

    return jsonify(success=True)


if __name__ == "__main__":
    app.run(debug=True)
