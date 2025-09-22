import json
import os

# Set the directory containing the .txt files
input_directory = 'C:/Users/Sicaja/Desktop/SmartCodeACADEMY/0.0_Channel_topics/12_How_to_do_data_analyse_and_build_model_&_visialization/0_Data/1_Unzipped/0_Data'

# Set the output directory for the .json files
output_directory = 'C:/Users/Sicaja/Desktop/SmartCodeACADEMY/0.0_Channel_topics/12_How_to_do_data_analyse_and_build_model_&_visialization/0_Data/1_Unzipped/1_OutputData/\DataAfterScript_1.0'

# Create the output directory if it does not exist
os.makedirs(output_directory, exist_ok=True)

# Loop through all files in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith('.txt'):  # Check if the file is a .txt file
        file_path = os.path.join(input_directory, filename)
        new_filename = os.path.splitext(filename)[0] + '.json'
        new_file_path = os.path.join(output_directory, new_filename)

        # Open the .txt file and read each line separately
        with open(file_path, 'r') as file:
            json_data = []
            for line in file:
                try:
                    # Load each line as JSON
                    data = json.loads(line)
                    json_data.append(data)
                except json.JSONDecodeError as e:
                    print(f"Failed to convert {filename}: Invalid JSON data. Error: {str(e)}")
                    break

            # Write the collected JSON objects to a .json file
            with open(new_file_path, 'w') as new_file:
                json.dump(json_data, new_file, indent=4)
                print(f"Converted {filename} to {new_filename} in the output directory")
