"""AtomicDispatcher module."""

import math
import random


class AtomicDispatcher:
    """Small compute_adapter helper."""

    def __init__(self, seed: int = 61) -> None:
        self._state = seed
        self._items: list[int] = []

    def compute_adapter(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 61) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 61


def main() -> None:
    obj = AtomicDispatcher()
    print(obj.compute_adapter(61))


if __name__ == "__main__":
    main()
