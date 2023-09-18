import csv

def extract_rows_between(input_csv, output_csv, start_row, end_row):
    try:
        with open(input_csv, 'r', newline='') as infile, open(output_csv, 'w', newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)

            # Copy header row to the output CSV file
            header = next(reader)
            writer.writerow(header)

            # Skip rows until reaching the start_row
            for _ in range(start_row - 1):
                next(reader)

            # Write rows between start_row and end_row (inclusive) to the output CSV
            for i, row in enumerate(reader, start=start_row):
                writer.writerow(row)
                if i == end_row:
                    break

        print(f"Rows {start_row} to {end_row} have been extracted to {output_csv}.")
    except FileNotFoundError:
        print("Input CSV file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Define the input CSV file and output CSV file
input_csv = 'profs.csv'
output_csv = 'trim.csv'

# Define the start and end row indices (1-based indexing)
start_row = 1  # Change this to your desired start row
end_row = 1000    # Change this to your desired end row

# Call the function to extract rows between start_row and end_row
extract_rows_between(input_csv, output_csv, start_row, end_row)
