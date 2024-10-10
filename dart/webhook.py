import hashlib
import hmac
import os


_WEBHOOK_SECRET = os.environ.get("DART_WEBHOOK_SECRET")
_ENCODED_WEBHOOK_SECRET = (
    _WEBHOOK_SECRET.encode() if _WEBHOOK_SECRET is not None else None
)


def is_signature_correct(payload: bytes, signature: str) -> bool:
    if _ENCODED_WEBHOOK_SECRET is None:
        raise RuntimeError("DART_WEBHOOK_SECRET environment variable is not set")
    expected_signature = hmac.new(
        _ENCODED_WEBHOOK_SECRET, payload, hashlib.sha256
    ).hexdigest()
    try:
        return hmac.compare_digest(expected_signature, signature)
    except TypeError:
        return False
