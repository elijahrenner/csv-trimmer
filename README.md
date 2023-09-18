# csv-trimmer
Simple Python script that extracts specific rows in a large datasets.

# instructions

```input_csv``` is the path to your original CSV file.

```output_csv``` is the path where the trimmed CSV file will be saved.

```start_row``` is the row number from which you want to start extracting (1-based indexing).

```end_row``` is the row number at which you want to stop extracting (inclusive, 1-based indexing).

Make sure to customize the values of ```input_csv```, ```output_csv```, ```start_row```, and ```end_row``` according to your specific requirements. When you run the script, it will create a new CSV file ('trim.csv') containing the specified rows from the input CSV.
