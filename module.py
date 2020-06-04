def find_module(modulename, filename=None):
    import imp
    import sys
    
    full_path = []
    if filename:
        full_path.append(os.path.dirname(os.path.abspath(filename)))
    full_path += sys.path
    fname = imp.find_module(modulename, full_path)
    return fname[1]


import os
print(find_module("paramiko"))
os.system("pause")