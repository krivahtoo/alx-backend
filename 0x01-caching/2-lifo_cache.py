#!/usr/bin/python3
""" LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines a LIFO caching system """

    def __init__(self):
        """ Initialize the class with the parent init method
        and set up LIFO tracking """
        super().__init__()
        self.last_key = None  # To keep track of the last added key

    def put(self, key, item):
        """ Assign the item to the key in cache_data using LIFO algorithm """
        if key is not None and item is not None:
            # Add the item to cache_data
            self.cache_data[key] = item

            # If we're exceeding the max, remove the last item added
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                if self.last_key is not None \
                        and self.last_key in self.cache_data:
                    del self.cache_data[self.last_key]
                    print("DISCARD:", self.last_key)

            # Update the last_key after any potential discard
            self.last_key = key

    def get(self, key):
        """ Return the value linked to key in cache_data,
        or None if key is None or not present """
        return self.cache_data.get(key, None)


if __name__ == '__main__':
    my_cache = LIFOCache()
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
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
