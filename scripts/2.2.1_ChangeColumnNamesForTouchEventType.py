import pandas as pd

# Define the file paths
input_file_path = r"C:\Users\Sicaja\Desktop\SmartCodeACADEMY\0.0_Channel_topics\12_How_to_do_data_analyse_and_build_model_&_visialization\0_Data\1_Unzipped\1_OutputData\DataAfterScript_1.9\DataAfterScript_1.9.xlsx"
output_file_path = r"C:\Users\Sicaja\Desktop\SmartCodeACADEMY\0.0_Channel_topics\12_How_to_do_data_analyse_and_build_model_&_visialization\0_Data\1_Unzipped\1_OutputData\DataAfterScript_2.2.1\DataAfterScript_2.2.1.xlsx"

# Load the data
data = pd.read_excel(input_file_path)

# Rename the columns
new_column_names = {col: col.replace('j_eT', 'j_eT_event_type') for col in data.columns}
data.rename(columns=new_column_names, inplace=True)

# Save the new file
data.to_excel(output_file_path, index=False)

print(f"Column names have been updated and the file has been saved to {output_file_path}")
