import csv

filename = "cidade_rs.csv"
separator = ";"

# Open the CSV file with the appropriate encoding
with open(filename, 'r', newline='', encoding='latin-1') as file:
    reader = csv.reader(file, delimiter=separator)

    # Read the header row
    header = next(reader)

    # Find the indices of the columns you want to extract
    column_indices = [header.index("cidades")]

    # Initialize a list to store the extracted column data
    extracted_columns = [[] for _ in range(len(column_indices))]

    # Extract the data for the specified columns
    for row in reader:
        for i, index in enumerate(column_indices):
            extracted_columns[i].append(row[index])

# Print the extracted column data
for column_data in extracted_columns:
    print(column_data)