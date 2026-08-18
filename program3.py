#Automated CSV File Inspector and Data Exporter
import pandas as pd

# Ask for input file name
filename = input("Enter CSV/TSV file name: ")

# Ask for file type
file_type = input("Enter file type (csv/tsv): ").lower()

# Set separator according to file type
if file_type == "tsv":
    separator = "\t"
else:
    separator = ","

# Read the file
df = pd.read_csv(filename, sep=separator)

# Display the dataset
print("\nDataset:")
print(df)

# Display number of rows and columns
print("\nNumber of rows and columns:")
print(df.shape)

# Display data types
print("\nData types:")
print(df.dtypes)

# Display dataset information
print("\nDataset information:")
df.info()

# Ask for column to filter
column = input("\nEnter column name for filtering: ")

# Ask for minimum value
value = float(input("Enter minimum value: "))

# Filter the data
filtered_df = df[df[column] >= value]

# Display filtered data
print("\nFiltered Dataset:")
print(filtered_df)

# Ask for output file name
output_file = input("\nEnter output CSV file name: ")

# Save filtered data
filtered_df.to_csv(output_file, index=False)

print("\nFiltered data saved successfully!")