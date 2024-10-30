#!/usr/bin/env python3
"""
2. Hypermedia pagination
"""

import csv
import math
from typing import Dict, List


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple containing the start and end indexes
    for pagination, where page numbers are 1-indexed.

    Arguments:
    page -- the current page number (1-indexed)
    page_size -- the number of items per page

    Returns:
    A tuple (start_index, end_index)
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page from the dataset."""
        assert isinstance(page, int) and page > 0, \
            'page must be a positive integer'
        assert isinstance(page_size, int) and page_size > 0, \
            'page_size must be a positive integer'

        start_idx, end_idx = index_range(page, page_size)

        return self.dataset()[start_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Return a dictionary with pagination details and dataset page."""
        data = self.get_page(page, page_size)

        # Calculate total number of pages
        dataset_size = len(self.dataset())
        total_pages = math.ceil(dataset_size / page_size)

        # Determine next and previous pages
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages,
        }


if __name__ == "__main__":
    server = Server()

    print(server.get_hyper(1, 2))
    print("---")
    print(server.get_hyper(2, 2))
    print("---")
    print(server.get_hyper(100, 3))
    print("---")
    print(server.get_hyper(3000, 100))
