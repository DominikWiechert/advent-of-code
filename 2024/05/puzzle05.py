from helper_functions import get_input
##################################
### --- Day 5: Print Queue --- ###
##################################

#--------------------------------------
# Classes
class RuleHashmap:
    def __init__(self):
        self.rules = {}

    def update_rules(self, rule: str):
        parts = rule.split('|')

        if int(parts[0]) in self.rules:
            self.rules[int(parts[0])].append(int(parts[1]))
        else:
            self.rules[int(parts[0])] = [int(parts[1])]

    def is_line_correct(self, line: list[int]) -> bool:
        for i in range(1, len(line)):
            if not self.is_element_correct_in_line(line, i):
                return False
        return True

    def is_element_correct_in_line(self, line: list[int], i):
        if line[i] in self.rules.keys():
            for number in line[0:i]:
                if number in self.rules[line[i]]:
                    return False
        return True

    def reorder_line(self, line: list[int]) -> list[int]:
        i = 0

        while i < len(line):
            if self.is_element_correct_in_line(line, i):
                i += 1
                continue
            else:
                line = swap_elements_in_list(line, i, i - 1)
                i = 0

        return line

    def get_middle_element_of_line(self, line: list[int]) -> int:
        return line[int((len(line) / 2))]

def parse_string_as_int_list(s: str) -> list[int]:
    parts = s.split(',')
    return [int(x) for x in parts]

def swap_elements_in_list(l: list, i: int, j: int) -> list:
    mem = l[i]
    l[i] = l[j]
    l[j] = mem
    return l

def get_sum_of_correct_lines(data: list[str]) -> int:
    rule_map = RuleHashmap()
    n = 0
    for line in data:
        if line == "":
            continue
        elif line.count("|") == 1:
            rule_map.update_rules(line)
        elif line.count(",") >= 1:
            line = parse_string_as_int_list(line)
            if rule_map.is_line_correct(line):
                n += rule_map.get_middle_element_of_line(line)
    return n

def get_sum_of_incorrect_lines(data: list[str]) -> int:
    rule_map = RuleHashmap()
    n = 0
    for line in data:
        if line == "":
            continue
        elif line.count("|") == 1:
            rule_map.update_rules(line)
        elif line.count(",") >= 1:
            line = parse_string_as_int_list(line)
            if not rule_map.is_line_correct(line):
                line = rule_map.reorder_line(line)
                n += rule_map.get_middle_element_of_line(line)
    return n

if __name__ == '__main__':
    input_lines = get_input()
    print(get_sum_of_correct_lines(input_lines))
    print(get_sum_of_incorrect_lines(input_lines))