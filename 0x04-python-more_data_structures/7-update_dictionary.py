#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary.items():
        a_dictionary.update(key, value)
    else:
        a_dictionary.setdefault(key, value)