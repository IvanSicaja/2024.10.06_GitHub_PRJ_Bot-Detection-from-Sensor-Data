import pandas as pd

# Define input and output file paths
input_file_path = r"C:\Users\Sicaja\Desktop\SmartCodeACADEMY\0.0_Channel_topics\12_How_to_do_data_analyse_and_build_model_&_visialization\0_Data\1_Unzipped\1_OutputData\DataAfterScript_1.5\j_eT.xlsx"
output_file_path = r"C:\Users\Sicaja\Desktop\SmartCodeACADEMY\0.0_Channel_topics\12_How_to_do_data_analyse_and_build_model_&_visialization\0_Data\1_Unzipped\1_OutputData\DataAfterScript_1.9\DataAfterScript_1.9.xlsx"

# Read the Excel file
df = pd.read_excel(input_file_path)

# Function to remove everything after the first comma in each cell
def remove_after_first_comma(cell_value):
    if isinstance(cell_value, str):
        comma_index = cell_value.find(',')  # Find the index of the first comma
        if comma_index != -1:
            return cell_value[:comma_index]  # Return everything before the first comma
    return cell_value  # Return the original value if it's not a string or doesn't contain a comma

# Apply the function to each cell in the DataFrame
df = df.applymap(remove_after_first_comma)

# Save the modified DataFrame to a new Excel file
df.to_excel(output_file_path, index=False)

print("File has been created at:", output_file_path)
