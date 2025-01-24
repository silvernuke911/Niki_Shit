import csv

# Input and output CSV file names
input_file = r'data\RTDdata.csv'
output_file = r'data\RTDdataN.csv'

# Read the input CSV file
with open(input_file, 'r') as infile:
    reader = csv.reader(infile)
    data = list(reader)

# Transpose and regroup the data
transposed_data = list(zip(*[iter(data[0])]*3)) + list(zip(*[iter(data[1])]*3))

# Write the transposed data to the output CSV file
with open(output_file, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    for group in transposed_data:
        writer.writerow(group)

print(f"Data regrouped and saved to {output_file}")
