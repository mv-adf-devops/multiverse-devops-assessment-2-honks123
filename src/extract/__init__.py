def get_input(filename):
    rows = []
    try:
        with open(filename, 'r') as f:
            for line in f.readlines():
                rows.append(line)
    except OSError as e:
        print(f"unable to open {filename}: {e}")
    return rows
