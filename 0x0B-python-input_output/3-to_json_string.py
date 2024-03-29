#!/usr/bin/python3
"""This module defines a file-appending function"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of a string object"""
    return json.dumps(my_obj)
