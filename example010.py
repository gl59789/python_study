"""
import subprocess

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)

print(result.returncode)
print(result.stdout)
print(result.stdout.split())
print(result.stdout.decode().split())


import os
import subprocess

my_env = os.environ.copy()
my_env['PATH'] = os.pathsep.join(["/opt/myapp/", "my_env[PATH]"])

result = subprocess.run(["myapp"], env=my_env, capture_output=True)
print(result.stderr)
"""

import re
def show_time_of_pid(line):
#    pattern = r"(^\w{3} \d{1,2} \d{1,2}:\d{2}:\d{2}) \[(\d+)\]"
    """
    Args:
        line:
    """
    pattern = r"\[(\d+)\]"
    result = re.search(pattern, line)
#    return "{} pid: {}".format(result[1], result[2])
    return result[0]

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440

print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187

print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187

print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440

print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807

print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440

print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440