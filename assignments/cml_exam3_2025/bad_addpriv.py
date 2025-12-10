# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 16:23:29 2025

@author: IFrommer
"""
privilege_names = ['lead','vote','attend']

class Member():
    def __init__(self, name, privileges = [0,0,1]):
        self._name = name
        self._privileges = privileges
        # self._rating = None       
        
    def get_name(self):
        return self._name
    
    def add_priv(self, priv_type):
        if priv_type == 'attend':
            self._privileges[1] = 1   # ERROR should be [2]
        elif priv_type == 'vote':
            self._privileges[1] = 1
        elif priv_type == 'lead':
            self._privileges[0] = 1    
   