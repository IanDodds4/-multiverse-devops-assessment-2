def get_input(filename):
    data = []
    with open(filename) as f:
        for line in f.readlines():
            data.append(line.strip().split(','))

    return data
