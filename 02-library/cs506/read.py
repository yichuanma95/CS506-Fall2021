def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    with open(csv_file_path, 'r') as f:
        data = [convert_numerical_data(line.strip().split(',')) for line in f]
    return data

def convert_numerical_data(line):
    for i, col in enumerate(line):
        if col.isnumeric(): line[i] = int(col)
        else: line[i] = col.split('\"')[1]
    return line
