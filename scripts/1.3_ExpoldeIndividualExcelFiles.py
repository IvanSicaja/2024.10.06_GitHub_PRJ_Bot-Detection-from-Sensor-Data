import os
import pandas as pd

input_directory = r"C:\Users\Sicaja\Desktop\SmartCodeACADEMY\0.0_Channel_topics\12_How_to_do_data_analyse_and_build_model_&_visialization\0_Data\1_Unzipped\1_OutputData\DataAfterScript_1.2"
output_directory = r"C:\Users\Sicaja\Desktop\SmartCodeACADEMY\0.0_Channel_topics\12_How_to_do_data_analyse_and_build_model_&_visialization\0_Data\1_Unzipped\1_OutputData\DataAfterScript_1.3"

# Ensure output directory exists
os.makedirs(output_directory, exist_ok=True)


def process_cell(cell):
    if pd.isna(cell):
        return [cell]  # Return as a list for compatibility
    return cell.split("],")


# Process each file
for filename in os.listdir(input_directory):
    if filename.endswith(".xlsx"):
        filepath = os.path.join(input_directory, filename)
        df = pd.read_excel(filepath)

        new_data = []

        for index, row in df.iterrows():
            new_row = []
            for cell in row:
                processed = process_cell(cell)
                new_row.extend(processed)
            new_data.append(new_row)

        # Create a new DataFrame from the processed data
        new_df = pd.DataFrame(new_data)

        # Save the processed DataFrame to a new Excel file in the output directory
        output_filepath = os.path.join(output_directory, filename)
        new_df.to_excel(output_filepath, index=False, header=False)

print("Processing complete.")
