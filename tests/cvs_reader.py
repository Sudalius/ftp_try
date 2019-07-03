import csv


def string_from_csv(path_to_csv):
    with open(path_to_csv, newline='') as file:
        csv_reader = csv.reader(file)
        first_line = next(csv_reader)
        return first_line
