#!/usr/bin/python3
"""
This module demonstrates LRU caching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    This class demonstrates LRU algorithm
    """
    def __init__(self):
        """
        Initializes the LRU cache class
        """
        super().__init__()
        self._track = []

    def put(self, key, item):
        """
        Updates the cache_data with item using
        LRU algorithm
        """
        can_pop = key not in self.cache_data
        max_out = len(self.cache_data) >= self.MAX_ITEMS
        if can_pop and max_out:
            del self.cache_data[self._track[0]]
            print('DISCARD: {}'.format(self._track[0]))
            self._track.remove(self._track[0])
        if key and item:
            if key in self.cache_data:
                self._track.remove(key)
            self._track.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        fetches the item in cache_data
        """
        if not key or key not in self.cache_data:
            return None
        self._track.remove(key)
        self._track.append(key)
        return self.cache_data[key]
