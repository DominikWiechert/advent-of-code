def get_input():
    with open('input.txt', 'r') as f:
        return f.read().splitlines()

def read_file_as_string(file_path):
    with open(file_path, 'r') as f:
        return f.read()