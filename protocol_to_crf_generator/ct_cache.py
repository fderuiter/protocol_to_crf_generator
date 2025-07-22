"""Simple in-memory LRU cache for terminology lookups."""

from __future__ import annotations

from collections import OrderedDict
from typing import Callable, Generic, TypeVar

T = TypeVar("T")


class CTCache(Generic[T]):
    """LRU cache storing the results of expensive lookups."""

    def __init__(self, fetch_func: Callable[[str], T], maxsize: int = 128) -> None:
        self.fetch_func = fetch_func
        self.maxsize = maxsize
        self._cache: OrderedDict[str, T] = OrderedDict()
        self.hits = 0
        self.misses = 0

    def lookup(self, key: str) -> T:
        """Return cached value for ``key`` or fetch and store it."""

        if key in self._cache:
            self.hits += 1
            self._cache.move_to_end(key)
            return self._cache[key]

        self.misses += 1
        value = self.fetch_func(key)
        self._cache[key] = value
        if len(self._cache) > self.maxsize:
            self._cache.popitem(last=False)
        return value

    def hit_rate(self) -> float:
        """Return cache hit rate as a float between 0 and 1."""

        total = self.hits + self.misses
        return (self.hits / total) if total else 0.0


__all__ = ["CTCache"]
