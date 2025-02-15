import pandas as pd

# Function to convert RA from hhmmss.s to degrees
def convert_ra_to_degrees(ra):
    if not ra or ra == 'nan':  # In case RA is empty, 'na', or missing
        return None
    # ra = str(ra).zfill(8)  # Ensure RA is a string with leading zeros
    hours = int(ra[:2])
    minutes = int(ra[2:4])
    seconds = float(ra[4:])
    
    # Convert to degrees
    ra_degrees = (hours * 15) + (minutes / 4) + (seconds / 240)
    return ra_degrees

def convert_ra_to_decimal(ra):
    if not ra or ra == 'nan':
        return None
    hours = int(ra[:2])
    minutes = int(ra[2:4])
    seconds = float(ra[4:])
    ra_decimal = hours + (minutes / 60) + (seconds / 3600) 
    return ra_decimal

# Function to convert Dec from ddmmss to degrees
def convert_dec_to_degrees(dec):
    if not dec or dec == 'nan':  # In case Dec is empty, 'na', or missing
        return None
    degrees = int(dec[1:3])  # For handling both positive and negative declinations
    minutes = int(dec[3:5])
    seconds = int(dec[5:])
    
    # Convert to degrees
    dec_degrees = degrees + (minutes / 60) + (seconds / 3600)
    
    # Handle negative declinations
    if dec[0] == '-':
        dec_degrees = -dec_degrees
    return dec_degrees

# Read the CSV with RA_2000 and Dec_2000 columns as strings to preserve leading zeros
data = pd.read_csv(r'data\bright_stars_extracted.csv', dtype={'RA_2000': str, 'Dec_2000': str})

# Drop rows where RA_2000, Dec_2000, or Vmag are missing
data_clean = data.dropna(subset=['RA_2000', 'Dec_2000', 'Vmag','Spct'])

# Create a DataFrame from the cleaned data
df = pd.DataFrame(data_clean)
print("Cleaned DataFrame:")
print(df)

# Convert RA and Dec to degrees decimal
df['RA_2000_Deg'] = df['RA_2000'].apply(convert_ra_to_degrees)
df['Dec_2000_Deg'] = df['Dec_2000'].apply(convert_dec_to_degrees)
df['RA_2000_HMS'] = df['RA_2000'].apply(convert_ra_to_decimal)

# Select relevant columns and save the result to a new CSV file
df_result = df[['Name', 'RA_2000_Deg','RA_2000_HMS', 'Dec_2000_Deg', 'Vmag', 'Spct']]
df_result.to_csv(r'data\bright_stars.csv', index=False)

# Print the converted DataFrame
print(df_result)
