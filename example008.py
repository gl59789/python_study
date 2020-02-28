"""import re
def check_sentence(text):
    result = re.search(r"^[A-Z][A-Za-z ]*[?.!]$", text)
    return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True


import re
def check_web_address(text):
    pattern = r"^([A-Za-z_\-\+]*[.])+[A-Za-z]+$"
    result = re.search(pattern, text)
    return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True


import re
def check_time(text):
    pattern = r"^([0-1]?[0-9]|[2][0-3]):([0-5][0-9])[ ]?(AM|am|PM|pm)$"
    result = re.search(pattern, text)
    return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False



import re
def long_words(text):
    pattern = r"\b\w{7,}\b"
    result = re.findall(pattern, text)
    return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []
"""

import re
def extract_pid(log_line):
    regex = r"\[(\d+)\]: ([A-Z]+)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)