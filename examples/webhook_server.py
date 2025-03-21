#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# README: https://help.itsdart.com/articles/9024895-webhooks


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
    match event_type:
        case "task.created":
            task = event["data"]["model"]  # The task that was created
            print(f"Task created:\n{task}")
        case "task.updated":
            data = event["data"]
            task = data["model"]  # The new version of the task that was updated
            old_task = data["oldModel"]  # The old version of the task that was updated
            print(f"Task updated from:\n{old_task}\nfrom:\n{task}")
        case "task.deleted":
            task = event["data"]["model"]  # The task that was deleted
            print(f"Task deleted:\n{task}")
        case "doc.created":
            doc = event["data"]["model"]  # The doc that was created
            print(f"Doc created:\n{doc}")
        case "doc.updated":
            data = event["data"]
            doc = data["model"]  # The new version of the doc that was updated
            old_doc = data["oldModel"]  # The old version of the doc that was updated
            print(f"Doc updated from:\n{old_doc}\nfrom:\n{doc}")
        case "doc.deleted":
            doc = event["data"]["model"]  # The doc that was deleted
            print(f"Doc deleted:\n{doc}")
        case "comment.created":
            comment = event["data"]["model"]  # The comment that was created
            print(f"Comment created:\n{comment}")
        case _:
            # Unexpected event type
            print(f"Unhandled event type: {event_type}")
            return jsonify(success=False)

    return jsonify(success=True)


if __name__ == "__main__":
    app.run(debug=True)
