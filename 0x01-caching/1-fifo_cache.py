#!/usr/bin/python3
""" FIFOCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines a FIFO caching system """

    def __init__(self):
        """
        Initialize the class with the parent init method and set up FIFO queue
        """
        super().__init__()
        self.order = []  # To keep track of the order of keys

    def put(self, key, item):
        """ Assign the item to the key in cache_data using FIFO algorithm """
        if key is not None and item is not None:
            # If key already exists, remove it to update its position
            if key in self.cache_data:
                self.order.remove(key)

            # Add the new key to the FIFO queue and cache data
            self.cache_data[key] = item
            self.order.append(key)

            # Check if we need to discard an item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # FIFO discard the oldest entry
                discard_key = self.order.pop(0)
                del self.cache_data[discard_key]
                print("DISCARD:", discard_key)

    def get(self, key):
        """ Return the value linked to key in cache_data,
        or None if key is None or not present """
        return self.cache_data.get(key, None)


if __name__ == '__main__':
    my_cache = FIFOCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    my_cache.put("F", "Mission")
    my_cache.print_cache()
