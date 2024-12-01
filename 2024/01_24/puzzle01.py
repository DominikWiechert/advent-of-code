from helper_functions import get_input

def split_input_lists(contents: list[str]) -> [list[int], list[int]]:
    data = get_input()
    list_left = []
    list_right = []

    for r in data:
        contents = r.split("   ")
        list_left.append(int(contents[0]))
        list_right.append(int(contents[1]))

    return list_left, list_right

def print_similarity_score():
    list_left, list_right = split_input_lists(get_input())

    similarity_score = 0
    for item in list_left:
        similarity_score += item * list_right.count(item)

    print(f'Similarity Score: {similarity_score}')

def print_absolute_distance():
    list_left, list_right = split_input_lists(get_input())
    list_left.sort()
    list_right.sort()

    abs_distance = 0
    for i in range(0, len(list_left)):
        abs_distance += max(list_left[i], list_right[i]) - min(list_left[i], list_right[i])

    print(f'Absolute Distance: {abs_distance}')

if __name__ == '__main__':
    print_absolute_distance()
    print_similarity_score()
