# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 13:21:43 2025 @author: IFrommer
This was from some initial testing but eventually will be superceded.
"""

import sys
import os

# Add repo root to sys.path so we can import graderlib
sys.path.append(os.path.abspath
                (os.path.join(os.path.dirname(__file__), "../../")))

from graderlib.tester import safe_construct
from reference import Restaurant as RefRestaurant

# normal constructor (should succeed)
ok1, obj1 = safe_construct(RefRestaurant, "Alice", "Italian")
print("Test 1 - normal init:")
print("Success:", ok1)
print("Object:", obj1)
print("Name:", obj1.get_name() if obj1 else "N/A")
print()


# we can wrap a failing constructor in a dummy class
# so imagine DummyRestaurant being the class from a student's code that is
#  wrong in that it crashes out no matter what
class DummyRestaurant:
    def __init__(self, name, cuisine):
        raise ValueError("Constructor failed!")

fallback_obj = RefRestaurant("Fallback", "French")
ok2, obj2 = safe_construct(
    DummyRestaurant, "Alice", "Italian", fallback=fallback_obj)

print("Test 2 - failing init, fallback used:")
print("Success:", ok2)
print("Object:", obj2)
print("Name:", obj2.get_name() if obj2 else "N/A")