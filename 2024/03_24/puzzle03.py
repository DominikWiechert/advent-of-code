from helper_functions import read_file_as_string
import re

def get_sum_of_data(data):
    s = 0
    matches = re.findall(r'mul\((\d+),(\d+)\)', data)

    for a, b in matches:
        s += int(a) * int(b)
    return s

def get_sum_of_enabled_data(data):
    enabled = True
    s = 0
    matches = re.findall(r'(do\(\))|(don\'t\(\))|mul\((\d+),(\d+)\)', data)

    for do, dont, a, b in matches:
        if dont:
            enabled = False
            continue
        if do:
            enabled = True
            continue
        if not enabled: continue
        s += int(a) * int(b)
    return s

if __name__ == '__main__':
    data = read_file_as_string('input.txt')
    s1 = get_sum_of_data(data)
    s2 = get_sum_of_enabled_data(data)
    print(s1, s2)