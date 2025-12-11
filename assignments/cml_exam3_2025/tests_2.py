# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 13:53:31 2024

@author: ifrommer
"""
import sys, os
sys.path.append(os.path.abspath
                (os.path.join(os.path.dirname(__file__), "../../")))
from graderlib.tester import safe_construct, test_method
# going to try to include some of the above but not all

# from member_data_file_2 import member_data, member_names
inst_vars = ['_name', '_privileges']
privs = ['attend', 'vote', 'lead']
pd0 = ['Megan', [0,0,0]]
pd1 = ['Chris', [0,0,1]]
pd2 = ['Jordan', [1,0,1]]
member_data = [pd0, pd1, pd2]
ratings = [b[1][0] + 2 * b[1][1] + 4 * b[1][2] for b in member_data]
# test add_priv by adding each priv to pd0 and pd2 - results:
priv_data = [[0,0,1],[0,1,1],[1,1,1],[1,0,1],[1,1,1],[1,1,1]]
ratings_tests = [
 [[0, 0, 0], 0],
 [[0, 0, 1], 1],
 [[0, 1, 0], 2],
 [[0, 1, 1], 3],
 [[1, 0, 0], 4],
 [[1, 0, 1], 5],
 [[1, 1, 0], 6],
 [[1, 1, 1], 7]]

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

def test_init(cls, member_data):
    #  initialize test params and Member objects
    pts = 0;  msg = ''
    try:        
        name, p_list = member_data[0]
        p0 = cls(name, p_list.copy())
        name, p_list = member_data[1]
        p1 = cls(name, p_list.copy())
        name, p_list = member_data[2]
        p2 = cls(name, p_list.copy())
        result = [p0, p1, p2]
        pts += 2
        msg = '1a of 1(a-d): instantiating 3 objects PASSED'
    except:
        msg = 'Error instantiating member objects'; #print(msg)
        result = "ERROR"
    return pts, result, msg

def test_type(cls, p0):
    pts = 0; msg = ''
    try:
        assert type(p0) == cls
        msg = '1b of 1(a-d): obj type PASSED'
        pts += 1
    except:
        msg = 'Object is not type member'
        msg += f'It is are {type(p0)}'
    return pts, msg

def test_inst_vars(p0): 
    pts = 0; msg = ''
    stu_inst_vars = sorted(p0.__dict__.keys())
    try:
        assert stu_inst_vars == sorted(inst_vars)
        msg = '1c of 1(a-d): inst var collection PASSED'
        pts += 2
    except:
        msg = 'Wrong instance variables.\n'
        msg += f'Correct: {inst_vars}'
        msg += f'Student: {stu_inst_vars}'
    return pts, msg

def test_inst_var_values(p0):
    pts = 0; msg = ''
    try:
        assert p0._name == pd0[0]
        assert p0._privileges == pd0[1]
        msg = '1d of 1(a-d): simple inst var values PASSED'
        pts += 3
    except:
        msg = '1d of 1(a-d): Some instance variable value(s) is(are) wrong.'
        msg += f'Correct: {pd0}'
        msg += f'Student: {p0.__dict__}'
    return pts, msg

def test_get_name(student_cls, obj, reference_value):
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
                                   reference_value)
    if ok:
        pts = 5; note = '2: get_name PASSED'
    else:
        pts = 0   # hard-coded pts for now, put in POINTS["get_name"]
    return pts, result, note

def test_add_priv(student_cls, p0, p2):
    # note add_priv has no return value, hence the _ a few lines down
    pts = 0;  i=0; note = "3: add_priv "
    passed_all = True; extra_info = ''
    for p in [p0, p2]:
        for priv in privs:
            ok, _, msg = test_method(student_cls, p, 'add_priv', None, priv) 
            if ok: 
                try:
                    assert p._privileges == priv_data[i]
                    pts += 4/3   # 8 pts total;  6 cases
                except:
                    passed_all = False
                    extra_info += f' {i} {priv_data[i]}'
            else: 
                passed_all = False
                note += msg
            i += 1
    note += passed_all * " PASSED" 
    note += (1-passed_all) * " had at least one failure" + extra_info
    return ok, note, pts

def test_compute_rating(cls):
    pts = 0;  msg = '4: ';    extra_info = ''; all_ok = True
    for privs, actual_rating in ratings_tests:
        memb = cls('dummy_name',privs )
        ok, stu_rating, note = test_method(cls, memb, 'compute_rating', 
                                           actual_rating) 
        all_ok = all_ok and ok
        #print(privs, actual_rating, stu_rating, ok)            
        broken_meth = 'not found' in note.lower() or 'error' in note.lower()
        if not ok:
            if broken_meth:
                return all_ok, pts, msg + note
            else:  # incorrectly computed a rating - get failure info
                extra_info += f' {privs} stu:{stu_rating} true:{actual_rating} |'
        else:  # ok - award points
            pts += (1/len(ratings_tests)) * 8  # out of 8 PTS

    if extra_info:
        note = msg + " compute_rating had at least one failure:" + extra_info
    else:
        note = msg + 'compute_rating PASSED'
    return all_ok, pts, note

def test_lt(cls, member_data, compute_ok ):
    pts = 0;  msg = '6: ';    extra_info = ''; all_ok = True
    p0 = cls(*member_data[0])  # in increasing order
    p1 = cls(*member_data[1])
    p2 = cls(*member_data[2])
    test_cases = [[p0,p1,True],[p2,p1,False],[p2,p2,False]]
    # print(p0,p1,p2)
    if compute_ok:  # their compute_rating() is good; try their __lt__ as is
        for left_obj, right_obj, ref_value in test_cases:
            ok, returned_value, note = test_method(
                cls, left_obj, '__lt__', ref_value, right_obj) 
            broken_meth = 'not found' in note.lower() or 'error' in note.lower()
            all_ok = all_ok and ok
            if not ok:
                if broken_meth:
                    return all_ok, pts, msg + note
                else:  # incorrectly computed a rating - get failure info
                    extra_info += f' {left_obj}<{right_obj} stu:{returned_value} true:{ref_value} |'
            else:  # ok - award points
                pts += (1/len(test_cases)) * 8  # out of 8 PTS
                print('lt test passed: ',left_obj,'<',right_obj,'=',
                      ok,returned_value,note)
    else:
        # something like this  "monkeypatching"
        """student = Student(*args)
        # save old one
        student._original_compute = student.compute    
        # replace with fallback
        student.compute = lambda: fallback.compute(student)
        student.compute = student._original_compute
        """
        return False, 0, msg + ' did not test since their compute_rating was broken'
    if extra_info:
        note = msg + " __lt__ had at least one failure:" + extra_info
    else:
        note = msg + '__lt__ PASSED'
    return all_ok, pts, note

def test_repr(cls, member_data, out_file):
    # pts = 0;  msg = '6: ';    extra_info = ''; all_ok = True
    p0 = cls(*member_data[0])  # in increasing order
    p2 = cls(*member_data[2])

    with open(out_file, "a") as f:   # appending
        try:
            print(50*'*','\n',cls,'\n', file = f)
            print(p0, file=f)
            print(p2, file=f)
        except:
            print('test_repr failed for',cls, file = f)
    
        
#############
# STARTS HERE 
import importlib
# replace this with the student modules
#test_files = ["reference","lt_is_broke","reversed_ratings","bad_addpriv",
#              "bad_var","bad_init","really_bad_init"] 


import pathlib
base = pathlib.Path(__file__).parent       # exam3 directory
student_dir = base / "e3_2025_stu_work"
sys.path.insert(0, str(student_dir))


def grade_student():
    all_notes = {}
    out_file = "repr_output.txt"
    with open(out_file, "w") as f:
        f.write("=== NEW RUN: previous contents overwritten ===\n\n")
    
    # for file in ['howryalyssa_747_275703_member']: #test_files:
    for pyfile in student_dir.glob("*.py"):
        print("Loading:", pyfile.name)
        file = pyfile.stem  #pyfile.name.split('.')[0]
        cur_notes = []
        student_module = importlib.import_module(file)
        # Check if the Class is proplery named, if so get it
        student_cls, note = get_student_class(student_module)
        if student_cls is None:
            all_notes[file] = [[0,note]]
            continue   # skip rest of this iteration go to next one
        else:    
            pts, result, msg = test_init(student_cls, member_data)
            if result == "ERROR": 
                cur_notes.append([0,msg])
                continue
            cur_notes.append([2,msg])
            p0, p1, p2 = result
        
        pts, msg = test_type(student_cls, p0)
        cur_notes.append([pts,msg])

        pts, msg = test_inst_vars(p0)
        cur_notes.append([pts,msg])
        
        pts, msg = test_inst_var_values(p0)
        cur_notes.append([pts,msg])

        pts, result, msg = test_get_name(student_cls, p0,
                                          reference_value = pd0[0])
        cur_notes.append([pts,msg])

        ok, msg, pts = test_add_priv(student_cls, p0, p2)
        cur_notes.append([pts,msg])
        
        compute_ok, pts, msg = test_compute_rating(student_cls)
        cur_notes.append([pts,msg])
        
        lt_ok, pts, msg = test_lt(student_cls, member_data, compute_ok)
        cur_notes.append([pts,msg])
        
        all_notes[file] = cur_notes
        
        test_repr(student_cls, member_data, out_file)
        
    return all_notes

all_notes = grade_student()
print(all_notes)


#%%
# Print scores
scores = dict()
for k in all_notes:
    name = k.split('_')[0]
    total = sum([i[0] for i in all_notes[k]])
    scores[name] = total
    # print(f'{name:20s}:  {total:>4.2f}')
#print(scores)
import pandas as pd
series = pd.Series(scores)




"""
#%%  Development code
# =============================================================================
# from member import member
# score = tester()
# print('Score = ',score)
# 
# =============================================================================

#%% Main tester call
import importlib, inspect, os, shutil
f = os.listdir()
fs = [x for x in f if len(x) == 5]
bfs = ['BC','CV','BR','RL','DM','UJ','BD','DL']
#[fs.remove(bf+'.py') for bf in bfs ]
for file_name in ['CC.py']:#fs:
    stu_module_name = file_name[:-3]
    if 'member' in globals():
        del member
    stu_module = importlib.import_module(stu_module_name)
    print('\n',file_name)    
    member = getattr(stu_module, 'member')    
    score = tester()
    print('Score = ',score)


#%% Call the repr tester
for file_name in []:#fs:
    stu_module_name = file_name[:-3]
    if 'member' in globals():
        del member
    stu_module = importlib.import_module(stu_module_name)
    print('\n',file_name)    
    member = getattr(stu_module, 'member')    
    test_repr_1(stu_module_name)



"""
"""
if 'Restaurant' in globals():
    del Restaurant
stu_module_name = input('Enter student initials: ')
stu_module = importlib.import_module(stu_module_name)
Restaurant = getattr(stu_module, 'Restaurant')    
r0 = Restaurant(r_names[0], r_cuisines[0])
"""