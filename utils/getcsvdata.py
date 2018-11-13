import csv


def get_csv_data(filename):

    # Created an empty list
    rows = []

    # Open the file to read it
    data_file = open(filename, "r")

    # Read the file
    reader = csv.reader(data_file)

    # Skip the header from the file
    next(reader)

    # Iterate and add data to the list
    for row in reader:
        rows.append(row)

    return rows

