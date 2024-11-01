#!/usr/bin/python3
""" BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines a basic caching system without limit """

    def put(self, key, item):
        """ Assign the item to the key in cache_data
        if both key and item are not None """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Return the value linked to key in cache_data,
        or None if key is None or not present """
        return self.cache_data.get(key, None)


if __name__ == '__main__':
    my_cache = BasicCache()
    my_cache.print_cache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    print(my_cache.get("D"))
    my_cache.print_cache()
    my_cache.put("D", "School")
    my_cache.put("E", "Battery")
    my_cache.put("A", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
