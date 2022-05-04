#!/usr/bin/env python3
"""
This module demonstrates generating
Indexes for a list of data
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    This returns a range of indexes with
    start and end indexes used to access
    a list of data
    """
    return ((page - 1 * page_size), (page * page_size))
