import psutil
import subprocess


src = "<source-path>" # replace <source-path> with the source directory
dest = "<destination-path>" # replace <destination-path> with the destination directory

subprocess.call(["rsync", "-arq", src, dest])




print(psutil.cpu_percent())

print(psutil.disk_io_counters())
print(psutil.net_io_counters())
