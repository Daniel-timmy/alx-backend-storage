#!/usr/bin/env python3
"""lists all documents in a collection
"""


import pymongo


def list_all(mongo_collection):
    """Return an empty list if no document in the collection"""
    if not mongo_collection:
        return []
    docs = mongo_collection.find()
    return [doc for doc in docs]
