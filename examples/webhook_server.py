#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# README: https://its-dart.notion.site/27064491a4694d0fb2b27d8294a6e3fa


import hashlib
import hmac
import json
import os

from flask import Flask, jsonify, request


WEBHOOK_SECRET = os.environ.get("DART_WEBHOOK_SECRET")


app = Flask(__name__)


def is_signature_correct(secret: bytes, payload: bytes, actual_signature: str) -> bool:
    expected_signature = hmac.new(secret, payload, hashlib.sha256).hexdigest()
    try:
        return hmac.compare_digest(expected_signature, actual_signature)
    except TypeError:
        return False


@app.route("/", methods=["POST"])
def webhook():
    payload = request.data

    # Parse the event
    try:
        event = json.loads(payload)
    except TypeError as ex:
        print(f"Webhook error while parsing event: {ex}")
        return jsonify(success=False)

    if WEBHOOK_SECRET:
        # Verify the signature of the event
        signature = request.headers.get("Dart-Signature")
        if not is_signature_correct(WEBHOOK_SECRET.encode(), payload, signature):
            print("Webhook signature verification failed")
            return jsonify(success=False)

    # Handle the event
    event_type = event["type"]
    if event_type == "task.created":
        task = event["data"]  # contains details of the task that was created
        print(f"Task created:\n{json.dumps(task, indent=2)}")
    elif event_type == "task.updated":
        task = event["data"]  # contains details of the task that was updated
        print(f"Task updated:\n{json.dumps(task, indent=2)}")
    elif event_type == "task.deleted":
        task = event["data"]  # contains details of the task that was deleted
        print(f"Task deleted:\n{json.dumps(task, indent=2)}")
    else:
        # Unexpected event type
        print(f"Unhandled event type: {event_type}")
        return jsonify(success=False)

    return jsonify(success=True)


if __name__ == "__main__":
    app.run(debug=True)
