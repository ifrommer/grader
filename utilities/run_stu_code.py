#%% Main tester call  didn't end up using much
import importlib, inspect, os, shutil
f = os.listdir()

fs = [x for x in f if x[0] !='_' if x.endswith('.py')]
print(fs)

#bfs = ['BC','CV','BR','RL','DM','UJ','BD','DL']
#[fs.remove(bf+'.py') for bf in bfs ]


for file_name in fs:
    stu_module_name = file_name[:-3]
    #if 'member' in globals():
    #    del member
    stu_module = importlib.import_module(stu_module_name)
    print('\n',file_name)    
    #member = getattr(stu_module, 'member')    
    #score = tester()
    #print('Score = ',score)