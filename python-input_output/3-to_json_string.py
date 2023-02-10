#!/usr/bin/python3
"""Defines a string-to-json function """
import json


def to_json_string(my_obj):
    """ Return object to JSON """
    return json.dumps(my_obj)
