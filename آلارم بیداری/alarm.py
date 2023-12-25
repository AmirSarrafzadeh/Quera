import re
from datetime import datetime, timedelta

def is_valid_time_format(input_string):
    pattern = re.compile(r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$')
    return bool(pattern.match(input_string))

def time_difference(time_str1, time_str2):
    format_str = '%H:%M:%S'
    time1 = datetime.strptime(time_str1, format_str)
    time2 = datetime.strptime(time_str2, format_str)
    if time1 > time2:
        time2 += timedelta(hours=24)
    elif time1 == time2:
        return "24:00:00"
    difference = time2 - time1
    difference_str = str(difference)
    if len(difference_str.split(":")[0]) == 1:
        difference_str = "0" + difference_str
    return difference_str


t1 = input()
t2 = input()
if is_valid_time_format(t1) and is_valid_time_format(t2):
    print(time_difference(t1, t2))








