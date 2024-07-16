import csv
import os
import pandas as pd

def convert_line_endings(file_path):
    with open(file_path, 'r', newline='') as infile:
        content = infile.read()
    
    # Replace CRLF with LF
    content = content.replace('\r\n', '\n')
    
    with open(file_path, 'w', newline='') as outfile:
        outfile.write(content)

def clean_csv(input_file, output_file):
    # Print the current working directory for debugging
    print("Current working directory:", os.getcwd())
    
    # Convert line endings before processing
    convert_line_endings(input_file)
    
    # Load the CSV data into a DataFrame
    df = pd.read_csv(input_file)
    
    # Remove rows where all elements are empty or whitespace only
    df_cleaned = df.replace(r'^\s*$', pd.NA, regex=True).dropna(how='all')
    
    # Write the cleaned data to the output CSV file
    df_cleaned.to_csv(output_file, index=False, header=False)

    print(f"Cleaned CSV file saved to {output_file}")

# Example usage with absolute paths
script_dir = os.path.dirname(os.path.abspath(__file__))
input_csv = os.path.join(script_dir, 'demo.csv')  # Absolute path to the input CSV file
output_csv = os.path.join(script_dir, 'demo-cleaned.csv')  # Absolute path to the output CSV file

# Ensure the output directory exists
os.makedirs(os.path.dirname(output_csv), exist_ok=True)

clean_csv(input_csv, output_csv)
