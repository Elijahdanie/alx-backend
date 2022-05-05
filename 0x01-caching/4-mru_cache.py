#!/usr/bin/env python3

"""
This module demonstrates MRU caching
"""

from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """
    This class demonstrates MRU caching
    """

    def __init__(self):
        """
        Initializes the MRU cache class
        """
        super().__init__()
        self._track = []

    def put(self, key, item):
        """
        Updates the cache_data with item using
        MRU algorithm
        """
        can_pop = key not in self._track
        max_out = len(self.cache_data) >= self.MAX_ITEMS
        if can_pop and max_out:
            _item = self._track.pop()
            del self.cache_data[_item]
            self._track.remove(_item)
        if key and item:
            if key not in self.cache_data:
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
