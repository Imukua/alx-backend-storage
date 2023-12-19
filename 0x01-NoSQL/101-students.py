#!/usr/bin/env python3
"""
script to avg and list scores
"""


def top_students(mongo_collection):
    pipeline = [
        {
            '$addFields': {
                'averageScore': {
                    '$avg': '$topics.score'
                }
            }
        },
        {
            '$sort': {
                'averageScore': -1
            }
        }
    ]

    result = mongo_collection.aggregate(pipeline)

    return list(result)
