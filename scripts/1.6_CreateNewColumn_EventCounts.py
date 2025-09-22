import os
import pandas as pd

# Path to the directory containing .xlsx files
directory = r"C:\Users\Sicaja\Desktop\SmartCodeACADEMY\0.0_Channel_topics\12_How_to_do_data_analyse_and_build_model_&_visialization\0_Data\1_Unzipped\1_OutputData\DataAfterScript_1.5"

# Path for the new file
output_file = r"C:\Users\Sicaja\Desktop\SmartCodeACADEMY\0.0_Channel_topics\12_How_to_do_data_analyse_and_build_model_&_visialization\0_Data\1_Unzipped\1_OutputData\DataAfterScript_1.6\DataAfterScript_1.6.xlsx"

# Initialize a dictionary to store row non-empty cell counts
row_counts = {}

# Iterate over each .xlsx file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".xlsx"):
        filepath = os.path.join(directory, filename)
        df = pd.read_excel(filepath)
        # Count the number of non-empty cells in each row and store it in the dictionary
        row_counts[filename[:-5]] = df.notnull().sum(axis=1)

# Create a DataFrame from the dictionary
df_counts = pd.DataFrame(row_counts)

# Add suffix to the headers
df_counts.columns = [col + "_event_counts" for col in df_counts.columns]

# Write the DataFrame to a new .xlsx file
df_counts.to_excel(output_file, index=False)
