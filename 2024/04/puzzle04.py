from helper_functions import get_input

def find_word_in_grid_all_dir(grid: list[str], word: str) ->  int:
    n_words = 0

    for i_row in range(0, len(grid)):
        for i_col in range(len(grid[i_row])):
            if grid[i_row][i_col] == word[0]:
                n_words += get_n_word_at_position(grid, word ="XMAS", char_id = 0, x_pos = i_row, y_pos = i_col, x_dir = 0, y_dir = 0)
    return n_words

def get_n_word_at_position(grid: list[str], word: str, char_id: int,
                           x_pos: int, y_pos: int, x_dir: int, y_dir:int) -> int:
    if char_id is len(word) - 1:
        return 1

    if char_id == 0:
        n = 0
        for x_dir in [-1, 0, 1]:
            if x_pos + x_dir < 0 or x_pos + x_dir > len(grid) - 1:
                continue
            for y_dir in [-1, 0, 1]:
                if (x_dir == 0 and y_dir == 0) or y_pos + y_dir < 0 or y_pos + y_dir > len(grid[0]) - 1:
                    continue

                if grid[x_pos + x_dir][y_pos + y_dir] == word[char_id + 1]:
                    n += get_n_word_at_position(grid, word=word, char_id=char_id + 1,
                                                x_pos=x_pos+x_dir, y_pos=y_pos+y_dir, x_dir=x_dir, y_dir=y_dir)
        return n

    if char_id > 0:
        if (x_pos + x_dir < 0 or x_pos + x_dir > len(grid) - 1 or
                y_pos + y_dir < 0 or y_pos + y_dir > len(grid[0]) - 1):
            return 0
        if grid[x_pos + x_dir][y_pos + y_dir] == word[char_id + 1]:
            return get_n_word_at_position(grid, word, char_id + 1,
                                          x_pos + x_dir, y_pos + y_dir, x_dir, y_dir)
        else:
            return 0

def find_n_mas_in_cross(grid: list[str]) -> int:
    n_words = 0
    for i_row in range(1, len(grid) - 1):
        for i_col in range(1, len(grid[0]) - 1):
            if grid[i_row][i_col] != "A":
                continue

            up_left = grid[i_row - 1][i_col - 1]
            up_right = grid[i_row - 1][i_col + 1]
            down_left = grid[i_row + 1][i_col - 1]
            down_right = grid[i_row + 1][i_col + 1]

            # Check 1st diagonal line. Elements can't be the same and have to be either 'S' or 'M'.
            if not(up_left != down_right and (up_left == 'S' or up_left == 'M') and (down_right == 'S' or down_right == 'M')):
                continue
            # Same as first diagonal line.
            if not(up_right != down_left and (up_right == 'S' or up_right == 'M') and (down_left == 'S' or down_left == 'M')):
                continue
            n_words += 1

    return n_words

if __name__ == '__main__':
    grid = get_input()
    n_xmas_all_dir = find_word_in_grid_all_dir(grid, "XMAS")
    n_mas_cross = find_n_mas_in_cross(grid)
    print(f'Part 1: {n_xmas_all_dir}\nPart 2: {n_mas_cross}')