
## OS and Path library experiments

import os
from pathlib import Path


"""
cwd = os.getcwd()
directory = "abc"
dir_path = os.path.join(cwd,directory)

if not os.path.exists(dir_path):
    os.makedirs(dir_path,exist_ok=True)
"""

x = ["abc/pqr/ijk/xyz.py","abc/pqr/xyz1.py","abc/pqr/xyz2.py","vishnu.txt","ratan.py"]

for i in x:
    i = Path(i)
    d,f = os.path.split(i)

    if d != "":
        os.makedirs(d,exist_ok=True)

    if (not os.path.exists(i)) or (os.path.getsize(i)==0):
        with open(i, "w") as f:
            pass

p=Path("abc/pqr/xyz1.py")          

print(os.path.getsize(p))

"""
for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
    else:
        print("file already exists")


"""

"""
print("---------------")
print(cwd)
print(f"This is current directory: {cwd}")
print("---------------")
directory = "abc"
dir_path = os.path.join(cwd,directory)
os.mkdir(dir_path)
print("---------------")
print("Directory '% s' created" % directory)
print(dir_path)
print("---------------")
"""

"""
directory1 = "pqr"
par_dir1 = "D:\Python Class\21_22nd Oct_23\LR_PROJ\abc"
dir_path1=os.path.join(par_dir1,directory1)
os.makedirs(dir_path1,exist_ok=False)
print("directory '% s' created" % directory1)
"""