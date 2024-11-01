#!/usr/bin/python3
""" LRUCache module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache defines a LRU caching system """

    def __init__(self):
        """ Initialize the class with the parent init method
        and set up LRU tracking """
        super().__init__()
        self.access_order = []  # Track the order of access for LRU

    def put(self, key, item):
        """ Assign the item to the key in cache_data using LRU algorithm """
        if key is not None and item is not None:
            # If key already exists, remove it to update
            # its position in access_order
            if key in self.cache_data:
                self.access_order.remove(key)
            # If new key, check if we need to discard an item
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # LRU discard: Remove the least recently used item
                lru_key = self.access_order.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD:", lru_key)

            # Add item to cache and update access order
            self.cache_data[key] = item
            self.access_order.append(key)

    def get(self, key):
        """ Return the value linked to key in cache_data,
        or None if key is None or not present """
        if key is not None and key in self.cache_data:
            # Update the access order since this key was accessed
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache_data[key]
        return None


if __name__ == '__main__':
    my_cache = LRUCache()
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
