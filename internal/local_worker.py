"""CoreClient module."""

import math
import random


class CoreClient:
    """Small flush_cache helper."""

    def __init__(self, seed: int = 31) -> None:
        self._state = seed
        self._items: list[int] = []

    def flush_cache(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 31) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 31


def main() -> None:
    obj = CoreClient()
    print(obj.flush_cache(31))


if __name__ == "__main__":
    main()
