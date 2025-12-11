# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 12:55:11 2025

@author: DDElmendorf
"""

class Member :
    
    def __init__(self,name,privilages):
        self._name = name
        self._privilages = privilages
        self._privilages_given= []
        
    def get_name(self):
        return self._name
    
    def add_priv(self,priv_type):
        self._privilages_given.append(priv_type)
        if priv_type == "attend":
            self._privilages[2] += 1
        elif priv_type == "vote":
            self._privilages[1] += 1
        elif priv_type == "lead":
            self._privilages[0] += 1
            
    def compute_rating(self):
        if self._privilages[0] == 1: # ==1 member has privilage
            lead_points = 4
        else: #self._privlages[0] == 0
            lead_points = 0
        if self._privilages[1] == 1:
            vote_points = 2
        else: #self._privilages[1] == 0
            vote_points = 0
        if self._privilages[2] == 1:
            attend_points = 1
        else: #self._privilages[2] == 0
            attend_points = 0
        total_points = lead_points + vote_points+ attend_points
        return total_points
    
    def __lt__(self, other):
        if self.compute_rating() > other.compute_rating():
            return False
        else:
            return True
    
    def __repr__(self):
        msg = f"{self._name} has these privilages:\n {self._privilages_given}"
        return msg
        
        












        