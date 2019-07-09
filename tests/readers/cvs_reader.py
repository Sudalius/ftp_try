import csv


def string_from_csv(path_to_csv, line_number):
    with open(path_to_csv, "r") as f:
        lines_array = []
        for line in f:
            lines_array.append(line)
    line = lines_array.__getitem__(line_number)
    print(line)
    return line


def dictionary_from_csv(path_to_csv, keys_column, values_column):
    with open(path_to_csv) as f:
        reader = csv.reader(f, delimiter=',')
        dic = {}
        for row in reader:
            keys = row[keys_column]
            values = row[values_column]
            dic[keys] = values
        for k in dic:
            print(k + " : " + dic[k])
        return dic
