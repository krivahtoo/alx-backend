#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a dictionary with pagination information that is
        resilient to deletions.
        """
        assert isinstance(index, int) and index >= 0, \
            "index must be a non-negative integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be a positive integer"

        # Ensure index is within bounds of the dataset keys
        data_keys = list(self.__indexed_dataset.keys())
        assert index in data_keys or index < len(data_keys)

        # Gather data starting from the current index,
        # until we've collected enough for the page
        data = []
        current_index = index
        while len(data) < page_size and current_index in \
                self.__indexed_dataset:
            data.append(self.__indexed_dataset[current_index])
            current_index += 1

        # Next index to query, or None if the end is reached
        next_index = current_index if current_index in \
            self.__indexed_dataset else None

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data,
        }


if __name__ == "__main__":
    server = Server()

    server.indexed_dataset()

    try:
        server.get_hyper_index(300000, 100)
    except AssertionError:
        print("AssertionError raised when out of range")

    index = 3
    page_size = 2

    print("Nb items: {}".format(len(server._Server__indexed_dataset)))

    # 1- request first index
    res = server.get_hyper_index(index, page_size)
    print(res)

    # 2- request next index
    print(server.get_hyper_index(res.get('next_index'), page_size))

    # 3- remove the first index
    del server._Server__indexed_dataset[res.get('index')]
    print("Nb items: {}".format(len(server._Server__indexed_dataset)))

    # 4- request again the initial index -> the first data retreives is
    # not the same as the first request
    print(server.get_hyper_index(index, page_size))

    # 5- request again initial next index -> same data page as the request 2-
    print(server.get_hyper_index(res.get('next_index'), page_size))
