#!/usr/bin/env python3
"""
changes all topics of school doc based on the name
"""


import pymongo


def update_topics(mongo_collection, name, topics):
    """changes all topics of school doc"""
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
