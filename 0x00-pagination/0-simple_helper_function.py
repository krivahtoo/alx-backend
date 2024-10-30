#!/usr/bin/env python3
"""
0. Simple helper function
"""


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


if __name__ == "__main__":
    res = index_range(1, 7)
    print(type(res))
    print(res)

    res = index_range(page=3, page_size=15)
    print(type(res))
    print(res)
