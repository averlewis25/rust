"""FastCache module."""

import math
import random


class FastCache:
    """Small handle_manager helper."""

    def __init__(self, seed: int = 28) -> None:
        self._state = seed
        self._items: list[int] = []

    def handle_manager(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 28) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 28


def main() -> None:
    obj = FastCache()
    print(obj.handle_manager(28))


if __name__ == "__main__":
    main()
