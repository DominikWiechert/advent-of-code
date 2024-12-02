from helper_functions import get_input

def first_puzzle():
    input = get_input()

    n_correct_reports = 0
    for line in input:
        vals = parse_input(line)
        if is_reactor_report_valid(vals, True):
            n_correct_reports += 1

    print(n_correct_reports)

def second_puzzle():
    input = get_input()

    n_correct_reports = 0
    for line in input:
        vals = parse_input(line)
        vals = list(map(int, vals))
        if is_reactor_report_valid(vals, False):
            n_correct_reports += 1

    print(n_correct_reports)

def is_reactor_report_valid(vals: list[int], dampener_used: bool):
    is_increasing = vals[1] > vals[0]
    for i in range(1, len(vals)):
        if is_increasing:
            is_valid_incline = vals[i] > vals[i - 1] and abs(vals[i] - vals[i - 1]) <= 3
        else:
            is_valid_incline = vals[i] < vals[i - 1] and abs(vals[i] - vals[i - 1]) <= 3

        if not is_valid_incline:
            if dampener_used:
                return False
            else:
                for j in range(0, len(vals)):
                    copy_vals = vals.copy()
                    copy_vals.pop(j)
                    if is_reactor_report_valid(copy_vals, True):
                        return True
                return False
    return True

def parse_input(in_string: str) -> list[int]:
    vals = in_string.split()
    vals = list(map(int, vals))
    return vals

if __name__ == '__main__':
    first_puzzle()
    second_puzzle()