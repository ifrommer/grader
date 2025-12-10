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
from reference import Member as RefMember

POINTS = {
    "init": 10,
    "init_fallback": 3,
    "get_name": 5,
    }

def get_student_class(module, class_name = "Member"):
    """ Try to extract student's Class. 
    Args:
        module (module): student's module
        class_name (str, optional): Defaults to "Member".
    Returns:
        result (object or None): object if Class is there, otherwise None
        note (str): message about what happened    """
    try:
        cls = getattr(module, class_name)
        result = cls;  note =  ""
    except AttributeError:
        result = None; 
        note =  f"Class `{class_name} not found in module {module.__name__}"
    return result, note

def test_init(module):
    """ test __init__ in the student's class
    Args:
        module (Python module object): module containing the student's 
          class we are testing.
    Returns:
        points (int)
        object (student object instance or fallback object instance)
    """
    ok, obj, notes = safe_construct(module, "Member", "Alice", [0,0,1],
                               fallback = RefMember("Alice",[0,0,1]))
    pts = POINTS["init"] if ok else POINTS["init_fallback"]
    return pts, obj, notes

def test_get_name(student_cls, obj):
    """
    Args:
        student_cls (class): the student's Class
        obj (object): either the student's instance or the fallback one
    Returns:
        pts (int): points
        result ( ): varies
        note (string): note about what happened in the test
    """    
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
    
    student_cls, note = get_student_class(module)
    if student_cls is None:
        return 0, all_notes + [note]
    
    pts, student_obj, note = test_init(module)  # student_obj might be the fallback
    total += pts
    all_notes.append(note)
    
    student_cls = getattr(module, 'Member')
    
    pts, student_name, note = test_get_name(student_cls, student_obj)
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


# Main loop through student files testing them
test_files = ["reference","bad_init","really_bad_init"] 
for file in ["reference","bad_init","really_bad_init"]:
    student_module = importlib.import_module(file)
    score, all_notes = grade_student(student_module)
    print(f'File: {file}\nTotal points: {score}\nNotes: {all_notes}')


    
    