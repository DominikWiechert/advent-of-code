from helper_functions import get_input
import time

def pad_grid(arr: list[str]) -> list[str]:
    c='%'
    arr = [c + line + c for line in arr]
    arr.insert(0, (len(arr[0])) * c)
    arr.append(len(arr[0]) * c)
    return arr

def search_guard(arr: list[str]):
    search_profile = '^'
    for x in range(1, len(arr)):
        if arr[x].count(search_profile):
            x = x
            y = arr[x].index(search_profile)
            x_dir = -1
            y_dir = 0
            return [x, y, x_dir, y_dir]
    raise RuntimeError("Schroedingers guard: He could be everywhere and nowhere")

def mark_step(visited: dict, x, y, x_dir, y_dir):
    if (x,y) in visited:
        visited[(x, y)].append((x_dir, y_dir))
    else:
        visited[(x, y)] = [(x_dir, y_dir)]
    return visited

def get_visited_places(data):
    data = pad_grid(data)
    x, y, x_dir, y_dir = search_guard(data)
    visited = {}

    while x > 0:
        next = data[x + x_dir][y + y_dir]
        if next in ['.', '^']:

            if (x,y) in visited:
                if (x_dir, y_dir) in visited[(x,y)]:
                    return -1

            visited = mark_step(visited, x, y, x_dir, y_dir)
            x += x_dir
            y += y_dir

        elif next == '%':
            visited = mark_step(visited, x, y, x_dir, y_dir)
            return visited

        elif next == '#':
            visited = mark_step(visited, x, y, x_dir, y_dir)
            x_dir, y_dir = rotate_directions(x_dir, y_dir)

def rotate_directions(x, y):
    return [y, -x]

def solve(data:list[str]) -> [int, int]:
    # Part 1
    visited_init = get_visited_places(data)
    s1 = len(visited_init)
    # Part 2
    s2 = 0
    for x_o in range(0, len(data)):
        for y_o in range(0, len(data[0])):
            if (data[x_o][y_o] == '^'): continue
            if (x_o+1, y_o+1) not in visited_init:
                # TODO: Remove padding from return value of get_visited_places
                continue
            data_copy = data.copy()
            data_copy[x_o] = data_copy[x_o][:y_o] + '#' + data_copy[x_o][y_o+1:]
            if get_visited_places(data_copy) == -1: s2+=1
    return [s1, s2]

if __name__ == '__main__':
    data = get_input()
    st = time.process_time()
    print(solve(data))
    res = time.process_time() - st
    print('CPU Execution time:', res, 'seconds')