#!/usr/bin/env python3
"""
lists all docs in mongo bd collection
"""


import pymongo


def list_all(mongo_collection):
    """Returns list of all documents in a collection"""
    if not mongo_collection:
        return []
    docs = mongo_collection.find()
    return [d for d in docs]
