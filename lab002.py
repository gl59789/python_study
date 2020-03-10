#!/usr/bin/env python3

from multiprocessing import Pool
import subprocess
import os
import re

def gen(namedir):
    dirlen = []
    for root, dirs, files in os.walk(namedir, topdown=false):
        for name in dirs:
            dirlen.append(os.path.join(root, name))
    return dirlen

def sync(ndir)
    src = ndir
    dest = re.sub("(/prod)", r"\1"+"_backup", src)
    print("Copying data from {} to {}".format(src, dest))
    subprocess.call(["rsync", "-arq", src, dest])


if __name__ == "__main__":
    d = gen("/home/student-00-228ab35bf156/data/prod")
    p = Pool(len(d))
    p.map(sync, d)
