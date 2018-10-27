#!/usr/bin/env python 
#
# fastclass - misc.py
# 
# Christian Werner, 2018-10-27

import collections
import itertools
from typing import Any, Iterable

# some helper functions

def flatten(iterable: Iterable, ltypes=collections.abc.Iterable) -> Any:
    """Convert nested into a flat list"""
    remainder = iter(iterable)
    while True:
        first = next(remainder)
        if isinstance(first, ltypes) and not isinstance(first, (str,bytes)):
            remainder = itertools.chain(first, remainder)
        else:
            yield first

def sanitize_searchstring(s: str, rstring: str = None) -> str:
    """Convert search term to clean folder string"""
    if rstring:
        ritems = rstring.strip().split(' ') if ' ' in rstring else [rstring]
        for rs in ritems:
            s = s.replace(rs.strip(), '')
    return s.strip().replace('"','').replace('&', 'and').replace(' ', '_')