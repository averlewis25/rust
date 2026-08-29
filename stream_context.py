"""LiteParser module."""

import math
import random


class LiteParser:
    """Small resolve_registry helper."""

    def __init__(self, seed: int = 95) -> None:
        self._state = seed
        self._items: list[int] = []

    def resolve_registry(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 95) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 95


def main() -> None:
    obj = LiteParser()
    print(obj.resolve_registry(95))


if __name__ == "__main__":
    main()
