#!/usr/bin/python3
def best_score(a_dictionary):
    result = ""
    score = 0

    if a_dictionary:
        for key, value in a_dictionary.items():
            if value > score:
                result = key
                score = value
        return result
    else:
        return None
