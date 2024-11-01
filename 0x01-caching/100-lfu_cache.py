#!/usr/bin/python3
""" LFUCache module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache defines a LFU caching system """

    def __init__(self):
        """ Initialize LFUCache with BaseCaching's init method,
        and set up frequency and usage tracking """
        super().__init__()
        self.frequency = {}    # Track the frequency of each key
        self.usage_order = []  # Track the usage order for LFU items

    def put(self, key, item):
        """ Add item to cache using LFU algorithm with LRU fallback for ties
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update item if it already exists and increase its frequency
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.usage_order.remove(key)
        else:
            # If cache size exceeds MAX_ITEMS, discard the LFU
            # (and LRU if tied) item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the minimum frequency among current cache items
                min_freq = min(self.frequency.values())
                # Find the least recently used item(s) with that frequency
                lfu_keys = [k for k in self.usage_order
                            if self.frequency[k] == min_freq]
                # The first key in usage_order with minimum frequency
                lfu_key = lfu_keys[0]

                # Remove the LFU item from cache
                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]
                self.usage_order.remove(lfu_key)
                print("DISCARD:", lfu_key)

            # Add the new item
            self.cache_data[key] = item
            self.frequency[key] = 1

        # Record this usage
        self.usage_order.append(key)

    def get(self, key):
        """ Retrieve item from cache by key, and update frequency
        and usage order if found """
        if key is None or key not in self.cache_data:
            return None

        # Increment the frequency of the accessed key
        self.frequency[key] += 1
        # Update the usage order for the accessed key
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]


if __name__ == '__main__':
    my_cache = LFUCache()
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
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()
    my_cache.put("L", "L")
    my_cache.print_cache()
    my_cache.put("M", "M")
    my_cache.print_cache()
