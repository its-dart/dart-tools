# TODO dedupe with the other order manager
from random import choices


_MIN_ORD = 1
_MAX_ORD = 256

_ORDER_CHARS = [chr(e) for e in range(_MIN_ORD, _MAX_ORD)]


class OrderException(Exception):
    pass


def _make_order_suffix():
    return "".join(choices(_ORDER_CHARS, k=4))


def _get_orders_between_recursive(start: str, end: str, count: int):
    max_len = max(len(start), len(end)) + 1
    for i in range(max_len):
        start_ord = ord(start[i]) if i < len(start) else _MIN_ORD
        end_ord = ord(end[i]) if i < len(end) else _MAX_ORD
        diff = end_ord - start_ord
        if diff <= 1:
            continue
        prefix = start[:i].ljust(i, chr(_MIN_ORD))
        if diff > count:
            frac = diff / (count + 1)
            return [
                prefix + chr(start_ord + round(frac * (j + 1))) for j in range(0, count)
            ]
        segs = (
            [start[i:]] + [chr(start_ord + j + 1) for j in range(diff - 1)] + [end[i:]]
        )
        tot_amount = 0
        amounts = []
        for j in range(diff):
            next_amount = round((count * (j + 1)) / diff) - tot_amount
            amounts.append(next_amount)
            tot_amount += next_amount
        res = []
        for j in range(diff):
            res += [
                prefix + e
                for e in _get_orders_between_recursive(segs[j], segs[j + 1], amounts[j])
            ]
        return res
    raise OrderException(f"failed to get {count} values between {start} and {end}")


def get_orders_between(start: str | None, end: str | None, count: int = 1):
    if count <= 0 or (bool(start) and bool(end) and start >= end):
        print(f"invalid request for {count} values between {start} and {end}")
        return [start or ""] * count
    return [
        e + _make_order_suffix()
        for e in _get_orders_between_recursive(start or "", end or "", count)
    ]
