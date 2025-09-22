import pandas as pd
import os

# Directory paths
input_dir = r"C:\Users\Sicaja\Desktop\SmartCodeACADEMY\0.0_Channel_topics\12_How_to_do_data_analyse_and_build_model_&_visialization\0_Data\1_Unzipped\1_OutputData\DataAfterScript_1.4_ManuallyBracketsRemoved"
output_dir = r"C:\Users\Sicaja\Desktop\SmartCodeACADEMY\0.0_Channel_topics\12_How_to_do_data_analyse_and_build_model_&_visialization\0_Data\1_Unzipped\1_OutputData\DataAfterScript_1.5"


# Function to get maximal row length for a DataFrame
def get_max_row_length(df):
    if df.empty:
        return 0
    return max(df.apply(lambda x: len(str(x)), axis=1))


# Process each file in the directory
for filename in os.listdir(input_dir):
    if filename.endswith(".xlsx"):
        file_path = os.path.join(input_dir, filename)

        # Read the Excel file
        try:
            df = pd.read_excel(file_path, header=None)  # Read without headers
        except Exception as e:
            print(f"Error reading file {filename}: {e}")
            continue

        try:
            # Calculate maximal row length
            max_row_length = get_max_row_length(df)
            print(f"Max row length for {filename}: {max_row_length}")

            # Create column names
            if max_row_length == 0:
                column_names = [f"{filename[:-5]}[0000]"]
            else:
                num_columns = df.shape[1]
                column_names = [f"{filename[:-5]}[{str(i).zfill(4)}]" for i in range(num_columns)]
            print(f"Number of columns in DataFrame: {df.shape[1]}")
            print(f"Number of generated column names: {len(column_names)}")

            # Insert the header row
            df.columns = column_names

        except Exception as e:
            print(f"Error processing file {filename}: {e}")
            continue

        # Save the modified DataFrame to a new Excel file
        output_file_path = os.path.join(output_dir, filename)
        try:
            df.to_excel(output_file_path, index=False)
            print(f"File {filename} processed and saved successfully.")
        except Exception as e:
            print(f"Error saving file {filename}: {e}")
