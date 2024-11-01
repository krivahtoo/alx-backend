#!/usr/bin/python3
""" MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache defines a MRU caching system """

    def __init__(self):
        """ Initialize the class with the parent init method
        and set up MRU tracking """
        super().__init__()
        self.access_order = []  # Track the order of access for MRU

    def put(self, key, item):
        """ Assign the item to the key in cache_data using MRU algorithm """
        if key is not None and item is not None:
            # If key already exists, remove it to update
            # its position in access_order
            if key in self.cache_data:
                self.access_order.remove(key)
            # If adding a new key and cache size exceeds MAX_ITEMS,
            # discard the most recently used item
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Most recently used is the last in access_order
                mru_key = self.access_order.pop(-1)
                del self.cache_data[mru_key]
                print("DISCARD:", mru_key)

            # Add item to cache and update access order
            self.cache_data[key] = item
            self.access_order.append(key)

    def get(self, key):
        """ Return the value linked to key in cache_data,
        or None if key is None or not present """
        if key is not None and key in self.cache_data:
            # Update the access order to reflect the recent access
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache_data[key]
        return None


if __name__ == '__main__':
    my_cache = MRUCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    print(my_cache.get("B"))
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
    my_cache.put("H", "H")
    my_cache.print_cache()
    my_cache.put("I", "I")
    my_cache.print_cache()
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()
