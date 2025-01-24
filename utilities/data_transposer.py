import pandas as pd
import os

def rotarod():
    # Read the CSV file into a DataFrame
    input_file = r'data\RTDdata.csv'
    data = pd.read_csv(input_file,header=None)
    print(data)
    # Initialize a new DataFrame for rearranged data
    rearranged_data = []

    # Process each row
    for index, row in data.iterrows():
        # Convert the row to a 3x3 matrix-like structure
        matrix = [row.values[i:i+3] for i in range(0, len(row), 3)]
        rearranged_data.extend(matrix)

    # Create a new DataFrame from the rearranged data
    rearranged_df = pd.DataFrame(rearranged_data)

    # Save the rearranged data to a new CSV file
    output_file = r'data\RTDdataN.csv'
    rearranged_df.to_csv(output_file, index=False, header=False)

    print(f"Rearranged data saved to {output_file}")
    os.startfile(output_file)

def hotplate():
    # Read the CSV file without a header
    input_file = r'data\RTDdata.csv'
    data = pd.read_csv(input_file, header=None)
    print(data)
    # Reshape the DataFrame into a single column
    rearranged_data = data.values.flatten()

    # Create a new DataFrame with the rearranged data
    rearranged_df = pd.DataFrame(rearranged_data, columns=["values"])

    # Save the rearranged data to a new CSV file
    output_file = r'data\RTDdataN.csv'
    rearranged_df.to_csv(output_file, index=False, header=False)

    print(f"Rearranged data saved to {output_file}")
    os.startfile(output_file)
hotplate()
#rotarod()
