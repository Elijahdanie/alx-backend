#!/usr/bin/env python3
"""
This module demonstrates caching using
FIFO Algorithm.
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):

    def __init__(self):
        """
        Initsilizes FIFOCache
        """
        super().__init__()
        self._track = []

    def put(self, key, item):
        """updates cache_data with item using FIFO"""
        can_pop = key not in self.cache_data
        max_out = len(self.cache_data) >= self.MAX_ITEMS
        if can_pop and max_out:
            del self.cache_data[self._track[0]]
            print('DISCARD: {}'.format(self._track[0]))
            self._track.remove(self._track[0])
        if key and item:
            self._track.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """gets item from cache_data"""
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
