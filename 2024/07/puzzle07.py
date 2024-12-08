from helper_functions import get_input

def parse_equation(equation: str) -> [int, list [int]]:
    eq = equation.split(":")
    return [int(eq[0]), [int(x) for x in eq[1].strip().split(" ")]]

def get_sum_of_correct_reports(input_data: list[str]) -> int:
    s1 = 0
    for line in input_data:
        eq_target, eq_parts = parse_equation(line)
        if is_equation_solvable(eq_target, eq_parts):
            s1 += eq_target

    return s1

def is_equation_solvable(target: int, eq_parts: list [int]):
    if len(eq_parts) == 1:
        return target == eq_parts[0]

    if target % eq_parts[-1] == 0 and is_equation_solvable(target // eq_parts[-1], eq_parts[:-1]):
        return True
    if target - eq_parts[-1] >= 0 and is_equation_solvable(target - eq_parts[-1], eq_parts[:-1]):
        return True
    return False

if __name__ == '__main__':
    data = get_input()
    print(get_sum_of_correct_reports(data))
