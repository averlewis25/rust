"""LiteCache module."""

import math
import random


class LiteCache:
    """Small load_collector helper."""

    def __init__(self, seed: int = 82) -> None:
        self._state = seed
        self._items: list[int] = []

    def load_collector(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 82) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 82


def main() -> None:
    obj = LiteCache()
    print(obj.load_collector(82))


if __name__ == "__main__":
    main()
