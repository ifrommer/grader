# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 09:03:13 2025

@author: IFrommer
"""

s= """Caleb + Alexis
Dax + Joe
Kimber + Brennan
Reid + Kirsten
Mara + Leo
Toby + Jeremias
Cole + Levi
Michael + Elyssia
Dylan + Christian"""

import os, shutil

src_rubric = 'rubric_AccessProject_v2.docx'
for pair in s.split('\n'):
    fname = pair.replace(' + ','') + '_Proj2Rubric.docx'
    print(fname)
    shutil.copy(src_rubric,fname)
    