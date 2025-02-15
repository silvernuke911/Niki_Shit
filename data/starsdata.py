import pandas as pd

# Define the column positions based on the byte-by-byte description
column_positions = [
    (4, 10),  # Name (bytes 5-14)
    (75, 83), # RA 2000 (bytes 61-75)
    (83, 90), # DE 2000 (bytes 85-90)
    (102, 107), # Vmag (bytes 103-107)
    (129), # Spectral type
]

# Open the Bright Star Catalog file
file_path = r'data\catalog.txt'  # Update with your file path
with open(file_path, 'r') as f:
    lines = f.readlines()

# Initialize lists to store the extracted data
names = []
ra_2000 = []
dec_2000 = []
vmags = []
spectra = []
# Process each line in the catalog file
for line in lines:
    # Extract each field based on the column positions
    name = line[column_positions[0][0]:column_positions[0][1]].strip()
    ra = line[column_positions[1][0]:column_positions[1][1]].strip()
    dec = line[column_positions[2][0]:column_positions[2][1]].strip()
    vmag = line[column_positions[3][0]:column_positions[3][1]].strip()
    spct = line[column_positions[4]].strip() #:column_positions[3][1]].strip()
    # Store the extracted data
    names.append(name)
    ra_2000.append(ra)
    dec_2000.append(dec)
    vmags.append(vmag)
    spectra.append(spct)
# Create a DataFrame to organize the extracted data
df = pd.DataFrame({
    'Name': names,
    'RA_2000': ra_2000,
    'Dec_2000': dec_2000,
    'Vmag': vmags,
    'Spct' : spectra
})

# Display the extracted data
print(df.head())

# Optionally, save the extracted data to a CSV file
df.to_csv(r'data\bright_stars_extracted.csv', index=False)
