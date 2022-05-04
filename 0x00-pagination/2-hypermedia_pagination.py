#!/usr/bin/env python3
""" return tuple"""

import csv
import math
from typing import Dict, List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initializes the server
        """
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        This returns a dictionary with the following keys:
        - total_pages: the total number of pages
        - current_page: the current page
        - next_page: the next page
        - previous_page: the previous page
        - data: the data within the current page
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        This returns a list of results within a range of indexes
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        range_ = index_range(page, page_size)
        data_set = self.dataset()
        len_ds = len(data_set)
        if len_ds < range_[0]:
            return []
        elif len_ds < range_[1]:
            return data_set[range_[0]:]
        elif len_ds >= range_[1]:
            return data_set[range_[0]:range_[1]]


def index_range(page: int, page_size: int) -> Tuple:
    """
    This returns a range of indexes with
    start and end indexes used to access
    a list of data
    """
    start = page - 1 * page_size
    end = start + page_size
    return (start, end)
