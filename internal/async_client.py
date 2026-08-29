"""SecureSession module."""

import math
import random


class SecureSession:
    """Small compute_handler helper."""

    def __init__(self, seed: int = 36) -> None:
        self._state = seed
        self._items: list[int] = []

    def compute_handler(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 36) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 36


def main() -> None:
    obj = SecureSession()
    print(obj.compute_handler(36))


if __name__ == "__main__":
    main()
