import csv

def transpose_csv(file_name):
    # Read data from the CSV file
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        data = [row for row in reader]

    # Flatten the data (if it's stored in multiple columns/rows)
    flat_data = [item for sublist in data for item in sublist]

    # Group the data into rows of three
    transposed_data = [flat_data[i:i+3] for i in range(0, len(flat_data), 3)]

    # Rewrite the CSV file with transposed data
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(transposed_data)

    print(f"The file '{file_name}' has been updated with transposed data.")
