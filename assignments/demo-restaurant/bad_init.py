# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 14:09:28 2025

@author: IFrommer
"""

class Restaurant:
    # intentional broken
    def __init__(self, name, cuisine):
        raise ValueError("Constructor failed!")
        

    # correct
    def get_name(self):
        return self._name        