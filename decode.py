# github.com/tb-net
# Decode downloaded scripts

import os, sys
from cryptography.fernet import Fernet
from mylibrary import file_list

word = '# github.com/tb-net'

key_path = '/root/.cred_fernet'
with open(key_path,'r') as f: key = Fernet(f.read())
if sys.argv[1]==None:
    F = file_list(r=True)
else:
    F = file_lsit(sys.argv[1], r=True)
F = [x for x in F if x[-2:]=='py' and x not in ignorelist]

for f in F:
    with open(f,'r') as x: data = x.read()
    if data[:19]!=word:
        with open(f,'rb') as x: data = x.read()
        decoded_file = key.decrypt(data)
        with open(f,'wb') as x: x.write(decoded_file)
            

