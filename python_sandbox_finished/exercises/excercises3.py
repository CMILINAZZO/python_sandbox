# Unit 3 Homework

import csv
import json

# Funtion that turns a csv file into a json file:

def csv_to_json(csv_filepath, json_filepath):
    try:
        with open(csv_filepath, 'r', newline='', encoding='utf-8') as csvfile:
            csvreader = csv.DictReader(csvfile)
            data = [row for row in csvreader]
        with open(json_filepath, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)

        print(f"Successfully converted '{csv_filepath}' to '{json_filepath}'")\

    except FileNotFoundError:
        print(f"Error: File not found - '{csv_filepath}'")
    except PermissionError:
        print(f"Error: Permission denied - '{csv_filepath}' or '{json_filepath}'")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
csv_to_json('customers.csv', 'customers.json')
