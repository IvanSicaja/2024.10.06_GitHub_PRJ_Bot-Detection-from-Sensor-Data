import pandas as pd
import os

# Define the relative paths
base_path = r"C:\Users\Sicaja\Desktop\SmartCodeACADEMY\0.0_Channel_topics\12_How_to_do_data_analyse_and_build_model_&_visialization"
input_file_path = os.path.join(base_path, r"0_Data\1_Unzipped\1_OutputData\2.0_OnlyRelevantColumns.xlsx")
output_directory = os.path.join(base_path, r"0_Data\1_Unzipped\1_OutputData\DataAfterScript_1.2")

# Check if the input file exists
if not os.path.exists(input_file_path):
    raise FileNotFoundError(f"The file at {input_file_path} was not found.")

# Check if the output directory exists, create if it doesn't
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Read the input Excel file
df = pd.read_excel(input_file_path)

# Create individual Excel files for each column
for column in df.columns:
    # Create a DataFrame for the current column
    column_df = df[[column]]

    # Sanitize column name for file name
    sanitized_column_name = "".join([c if c.isalnum() else "_" for c in column])

    # Define the output file path
    output_file_path = os.path.join(output_directory, f"DataAfterScript_{sanitized_column_name}.xlsx")

    # Save the column DataFrame to an Excel file
    column_df.to_excel(output_file_path, index=False)

print(f"Files have been saved to {output_directory}")
