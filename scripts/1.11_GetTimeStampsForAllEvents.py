import pandas as pd
import os

# Define the input and output directories
input_dir = "C:\\Users\\Sicaja\\Desktop\\SmartCodeACADEMY\\0.0_Channel_topics\\12_How_to_do_data_analyse_and_build_model_&_visialization\\0_Data\\1_Unzipped\\1_OutputData\\DataAfterScript_1.5"
output_dir = "C:\\Users\\Sicaja\\Desktop\\SmartCodeACADEMY\\0.0_Channel_topics\\12_How_to_do_data_analyse_and_build_model_&_visialization\\0_Data\\1_Unzipped\\1_OutputData\\DataAfterScript_1.11"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Process each Excel file in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".xlsx"):
        # Load the Excel file
        file_path = os.path.join(input_dir, filename)
        df = pd.read_excel(file_path)

        # Process each cell in the DataFrame
        for col in df.columns:
            df[col] = df[col].astype(str).apply(lambda x: x.split(',')[1] if ',' in x else '')

        # Rename the columns
        new_columns = {col: col.split('[')[0] + '_timestamp[' + col.split('[')[1] for col in df.columns}
        df.rename(columns=new_columns, inplace=True)

        # Save the edited DataFrame to the output directory
        output_path = os.path.join(output_dir, filename)
        df.to_excel(output_path, index=False)

print("Processing complete. Edited files saved to:", output_dir)
