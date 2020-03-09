import os
import datetime

#os.remove("test.txt")
#os.rename( "final_example.py", "final.py")
print(os.path.exists("final.py"))
#os.path.getsize()
timestamp = os.path.getmtime("final.py")
print(datetime.datetime.fromtimestamp(timestamp))

print(os.path.abspath("final.py"))
print(os.getcwd())
os.mkdir("new_dir")
os.chdir("new_dir")
print(os.getcwd())
os.chdir("/Users/kelee/Projects/Personal/python_course/")
os.rmdir("new_dir")