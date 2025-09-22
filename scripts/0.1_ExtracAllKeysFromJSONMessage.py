import os
import json

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Define the relative path to the JSON file
relative_file_path = os.path.join(script_dir, "0_Data/1_Unzipped/1_OutputData/OneMessageForDataUnderstanding.txt")

# Function to extract all keys from the JSON data
def extract_keys(json_data, parent_key=''):
    keys = []
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            full_key = f"{parent_key}.{key}" if parent_key else key
            keys.append(full_key)
            keys.extend(extract_keys(value, full_key))
    elif isinstance(json_data, list):
        for i, item in enumerate(json_data):
            full_key = f"{parent_key}[{i}]"
            keys.extend(extract_keys(item, full_key))
    return keys

# Read the JSON data from the file
with open(relative_file_path, 'r') as file:
    data = json.load(file)

# Extract all keys
keys = extract_keys(data)

# Print all keys
for key in keys:
    print(key)
