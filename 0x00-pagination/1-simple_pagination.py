#!/usr/bin/env python3
""" return tuple"""

import csv
import math
from typing import List, Tuple


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
        elif len_ds < range_[1] and len_ds > range_[0]:
            return data_set[range_[0]:]
        elif len_ds >= range_[1]:
            return data_set[range_[0]:range_[1]]


def index_range(page: int, page_size: int) -> Tuple:
    """
    This returns a range of indexes with
    start and end indexes used to access
    a list of data
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
