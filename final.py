#!/usr/bin/env python3

import re
import operator
from collections import Counter


def file_handle(logfile):
    """
    Args:
        logfile:
    """
    with open(logfile, "r") as f:
        return f.readlines()


def write_error_report(list_logs):
    """
    Args:
        list_logs:
    """
    regex = r"ERROR (([A-Za-z\']+ )+)"
    error_dict = {}
    for log in list_logs:
        error_message = re.findall(regex, log)
        if error_message:
            error_dict[error_message[0][0]] = error_dict.get(error_message[0][0], 0) + 1
    with open("error_message.csv", "w+") as f:
        f.write("Error, Count\n")
        for k in sorted(error_dict.items(), key=operator.itemgetter(1), reverse=True):
            f.write(k[0].strip()+', '+str(k[1])+'\n')
    f.close()


def write_per_user_report(list_logs):
    """
    Args:
        list_logs:
    """
    regex = r"(ERROR|INFO) .* \(([a-z]+(\.\w+)?)\)"
    user_dict = {}
    for log in list_logs:
        message = re.findall(regex, log)
        if not message:
            continue
        message_type, user, no_meaning = message[0]
        user_dict.setdefault(user, {})
        user_dict[user].setdefault(message_type, 0)
        user_dict[user][message_type] += 1

    with open("user_statistics.csv", "w") as f:
        f.write("Username, INFO, ERROR\n")
        for k in sorted(user_dict.items(), key=operator.itemgetter(0)):
            if not "ERROR" in k[1]:
                k[1]["ERROR"] = 0
            if not "INFO" in k[1]:
                k[1]["INFO"] = 0
            f.write(k[0]+', '+str(k[1]["INFO"])+', '+str(k[1]["ERROR"])+"\n")
    f.close()



logfile = "syslog.log"
write_error_report(file_handle(logfile))
write_per_user_report(file_handle(logfile))




    

