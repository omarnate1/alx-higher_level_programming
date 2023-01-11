#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tru Jan 11 15:13:37 2023
@author: Nathan Orobor
"""


def append_write(filename="", text=""):
    """
    Appends inputed text into a utf-8 encoded text file
    Arguments:
        filename (str): The name of the file to open
        text (str): The text to append
    Return:
        A file with appened text
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
