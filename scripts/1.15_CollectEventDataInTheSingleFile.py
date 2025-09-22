import pandas as pd
import os

# Define the input and output directories
input_dir = "C:\\Users\\Sicaja\\Desktop\\SmartCodeACADEMY\\0.0_Channel_topics\\12_How_to_do_data_analyse_and_build_model_&_visialization\\0_Data\\1_Unzipped\\1_OutputData\\DataAfterScript_1.14"
output_file = "C:\\Users\\Sicaja\\Desktop\\SmartCodeACADEMY\\0.0_Channel_topics\\12_How_to_do_data_analyse_and_build_model_&_visialization\\0_Data\\1_Unzipped\\1_OutputData\\DataAfterScript_1.15\\DataAfterScript_1.15.xlsx"

# Ensure the output directory exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Initialize an empty DataFrame for combining the data
combined_df = pd.DataFrame()

# Process each Excel file in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".xlsx"):
        # Load the Excel file
        file_path = os.path.join(input_dir, filename)
        df = pd.read_excel(file_path)

        # Combine the data
        combined_df = pd.concat([combined_df, df], axis=1)

# Save the combined DataFrame to a single Excel file
combined_df.to_excel(output_file, index=False)

print("Processing complete. Combined file saved to:", output_file)
