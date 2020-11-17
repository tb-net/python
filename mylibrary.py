# github.com/tb-net
# Library of commonly used python functions

import os
from os.path import isfile, join, isdir

def file_list(path=os.getcwd(),r=False,ignore=['.git','__pycache__']):
    ''' List all files in a location
    path:   directory for search, default = current
    r:      recursive, default = False
    ignore: ignore these folders, default = pycache, git
    '''
    if r:
        files = [join(path,f) for f in os.listdir(path) if isfile(join(path,f))]
        dirs = [d for d in os.listdir(path) if isdir(join(path,d)) and d not in ignore]
        for d in dirs:
            dir_files = file_list(join(path,d),r=True)
            if dir_files:
                for f in dir_files:
                    files.append(join(path,f))
    else:
        files = [join(path,f) for f in os.listdir(path) if isfile(f)]
    return files
