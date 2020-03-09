#!/usr/bin/env python3

import sys
import subprocess


def change_file_name(oldfile):
    """
    Args:
        oldfile:
    """
    with open(oldfile, "r") as f:
        for filename in f.readlines():
            old_filename = filename.strip()
            new_filename = old_filename.replace("jane", "jdoe")
            subprocess.run(["mv", old_filename, new_filename])
    f.close()

if __name__ == "__main__":
    oldfile = sys.argv[1]
    change_file_name(oldfile)