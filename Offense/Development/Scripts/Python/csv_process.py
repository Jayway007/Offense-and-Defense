import csv

def extract_cols(input_file, output_file):
    # Open the input file for reading
    with open(input_file, 'r') as in_file:
        # Create a reader object
        reader = csv.reader(in_file)
        # Skip the header row
        next(reader)
        # Open the output file for writing
        with open(output_file, 'w', newline='') as out_file:
            # Create a writer object
            writer = csv.writer(out_file)
            # Write the header row to the output file
            writer.writerow(['Column 2 & 3'])
            # Loop through each row in the input file
            for row in reader:
                # Extract the third and second columns
                col_2 = row[1]
                col_3 = row[2]
                # Combine the two columns and write to the output file
                writer.writerow([col_2 + ' ' + col_3])

# Call the function with the input and output file names
extract_cols('input.csv', 'output.csv')
