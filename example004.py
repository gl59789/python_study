import os

os.listdir("/Users/kelee/Projects/Personal/python_course/")

dir = "/Users/kelee/Projects/Personal/python_course/"

for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))