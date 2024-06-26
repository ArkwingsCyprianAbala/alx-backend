#!/usr/bin/env python3
"""
A function index_range that takes two integer arguments page and page_size.

Returns a tuple containing a start index and an end index.

Page numbers are 1-indexed, i.e. the first page is page 1.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple of size two containing a start index and an end index"""
    return ((page - 1) * page_size, page * page_size)
