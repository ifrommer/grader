# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 13:54:32 2025

@author: IFrommer
"""
import sys, os

# Add repo root to sys.path so we can import graderlib
sys.path.append(os.path.abspath
                (os.path.join(os.path.dirname(__file__), "../../")))
from graderlib.tester import safe_construct, test_method
from reference import Restaurant as RefRestaurant

POINTS = {
    "init": 10,
    "init_fallback": 3,
    "get_name": 5,
    }

def test_init(module):
    """ test __init__ in the student's class
    Args:
        module (Python module object): module containing the student's 
          class we are testing.
    Returns:
        points (int)
        object (student object instance or fallback object instance)
    """
    ok, obj, notes = safe_construct(module, "Restaurant", "Alice", "Italian",
                               fallback = RefRestaurant("Alice","Italian"))
    pts = POINTS["init"] if ok else POINTS["init_fallback"]
    return pts, obj, notes

def test_get_name(student_cls, obj):
    ok, result, note = test_method(student_cls, obj, "get_name", 
                                   reference_value = "Alice")
    pts = POINTS["get_name"] if ok else 0
    return pts, result, note


""" coming soon
def test_set_cuisine(obj):
        ...
"""

def grade_student(module):
    total = 0;    all_notes = []
    pts, student_obj, note = test_init(module)
    total += pts
    all_notes.append(note)
    
    pts, student_name, note = test_get_name(student_obj)
    print(student_name)
    total += pts
    all_notes.append(note)
    
    # then call the others and add their points
    # BUT fill in missing comments about what went wrong or what 
    #  their answer was
    return total, all_notes

# *** GPT has this in a separate script called run_grading.py but
#  I have it here at least for now
import importlib
# For now, reference.py is playing the role of the student,
#  but soon that will be replace by looping through the student module files

for file in ["reference","bad_init","really_bad_init"]:
    student_module = importlib.import_module(file)
    score, all_notes = grade_student(student_module)
    print(f'File: {file}\nTotal points: {score}\nNotes: {all_notes}')


    
    