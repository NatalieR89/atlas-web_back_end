#!/usr/bin/python3
""" MRUCache module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ MRUCache defines a MRU caching system """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache (MRU algorithm) """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            self.cache_data[key] = item
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key, _ = self.cache_data.popitem(last=True)
            print(f"DISCARD: {mru_key}")

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        self.cache_data.move_to_end(key)
        return self.cache_data[key]
