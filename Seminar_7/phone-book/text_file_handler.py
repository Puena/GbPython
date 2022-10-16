separator = " "


def init(iseparator):
    global separator
    separator = iseparator


def update_separator(iseparator):
    global separator
    separator = iseparator


def read(path, handler):
    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            data = line.strip().split(separator)
            handler(data[0], data[1], data[2], data[3])


def write(path, data):
    with open(path, 'w') as f:
        for line in data:
            f.write(separator.join(line) + "\n")
