#!/usr/bin/python3
"""Defines a string-to-json function """
import json


def from_json_string(my_str):
    """return string to json"""
    return json.dumps(my_str)
