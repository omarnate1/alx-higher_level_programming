#!/usr/bin/python3

def print_sort_dictionary(a_dictionary):
    for keys in sorted(a_dictionary.keys()):
        print('{}: {}'.format(keys, a_dictionary[keys]))
