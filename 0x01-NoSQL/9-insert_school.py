#!/usr/bin/env python3
"""function that inserts a new document in a collection
"""


import pymongo


def insert_school(mongo_collection, **kwargs):
    """Returns the new _id"""
    rdict = mongo_collection.insert(kwargs)
    return rdict
