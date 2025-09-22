import pandas as pd
import json
import os

# Set the input directory containing the .json files
input_directory = r"C:\Users\Sicaja\Desktop\SmartCodeACADEMY\0.0_Channel_topics\12_How_to_do_data_analyse_and_build_model_&_visialization\0_Data\1_Unzipped\1_OutputData\0.0_OriginalData"

# Set the output Excel file path
output_excel_file = r"C:\Users\Sicaja\Desktop\SmartCodeACADEMY\0.0_Channel_topics\12_How_to_do_data_analyse_and_build_model_&_visialization\0_Data\1_Unzipped\1_OutputData\DataAfterScript_1.7\DataAfterScript_1.7.xlsx"

# Initialize an empty list to store dataframes for each JSON file
dataframes = []

# Loop through all files in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith('.json'):  # Check if the file is a .json file
        file_path = os.path.join(input_directory, filename)

        # Open the .json file and read the JSON data
        with open(file_path, 'r') as file:
            try:
                # Load the JSON data
                json_data = json.load(file)

                # Normalize the JSON data into a dataframe
                df = pd.json_normalize(json_data)

                # Add a new column with the filename
                df['source_file'] = filename

                # Append the dataframe to the list
                dataframes.append(df)
            except json.JSONDecodeError as e:
                print(f"Failed to load {filename}: Invalid JSON data. Error: {str(e)}")

# Concatenate all dataframes into one
combined_df = pd.concat(dataframes, ignore_index=True)

# Write the combined dataframe to an Excel file
combined_df.to_excel(output_excel_file, index=False)

print(f"Successfully converted {len(dataframes)} JSON files to {output_excel_file}")
