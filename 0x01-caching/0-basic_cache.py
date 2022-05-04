#!/usr/bin/env python3
"""
This module demonstrates basic caching
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):

    def put(self, key, item):
        """updates cache_data with item"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        fetches an item from a cache
        """
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
