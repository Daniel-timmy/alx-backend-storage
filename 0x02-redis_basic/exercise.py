#!/usr/bin/env python3
"""class Cache"""
import uuid
from functools import wraps
from typing import Union, Optional, Callable

import redis


def count_calls(mtd: Callable) -> Callable:
    """returns a Callable"""
    key = mtd.__qualname__

    @wraps(mtd)
    def wrapper(self, *args, **kwargs):
        """wrapper for decorated function"""
        self._redis.incr(key)
        return mtd(self, *args, **kwargs)

    return wrapper


class Cache:
    """Cache clas which intializes redis"""
    def __init__(self):
        """store an instance of the Redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes a data argument and returns a string."""
        mkey = str(uuid.uuid4())
        self._redis.set(mkey, data)
        return mkey

    def get(self, key: str, fn: Optional[callable] = None) -> Union[str, bytes, int, float]:
        """convert the data back to the desired format"""
        val = self._redis.get(key)
        if fn:
            val = fn(val)
        return val

    def get_str(self, key: str) -> str:
        """returns string from byte format"""
        val = self._redis.get(key)
        val = val.decode("utf-8")
        return val

    def get_int(self, key: str) -> int:
        """returns string from byte format"""
        val = self._redis.get(key)
        try:
            val = val.decode("utf-8")
        except Exception:
            return 0
        return int(val)


