import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the file path
file_path = r"C:\Users\Sicaja\Desktop\SmartCodeACADEMY\0.0_Channel_topics\12_How_to_do_data_analyse_and_build_model_&_visialization\0_Data\1_Unzipped\1_OutputData\DataAfterScript_2.0_ManuallyCollectedAllExtractedFatures_TASK_2\DataAfterScript_2.0_numbers.xlsx"

# Load the necessary data
data = pd.read_excel(file_path)

# Extract relevant columns
timestamp_columns = [col for col in data.columns if col.startswith("j_eT_timestamp")]
data_columns = [col for col in data.columns if col.startswith("j_eT_event_data")]
color_column = "color"
source_file_column = "source_file"

# Get unique colors
unique_colors = data[color_column].unique()

# Define a colormap with distinct colors for each unique color entry
cmap = plt.get_cmap('tab10')
color_dict = {color_name: cmap(i) for i, color_name in enumerate(unique_colors)}

# Map each color to its corresponding source file
source_files = {color_name: data.loc[data[color_column] == color_name, source_file_column].iloc[0] for color_name in unique_colors}
legend_labels = {color_name: f"{color_name} - {source_files[color_name]}" for color_name in unique_colors}

# Plotting
fig = plt.figure(figsize=(16, 10))  # Increased figure size
ax = fig.add_subplot(111, projection='3d')

# Plotting all data points
for color_name in unique_colors:
    color_mask = data[color_column] == color_name

    for ts_col, data_col in zip(timestamp_columns, data_columns):
        ts_values = data.loc[color_mask, ts_col]
        data_values = data.loc[color_mask, data_col].str.split(',', expand=True)

        # Convert data values to numeric
        data_values = data_values.apply(pd.to_numeric, errors='coerce')

        # Filter out NaN values
        valid_mask = data_values.notna().all(axis=1)
        ts_values = ts_values[valid_mask]
        data_values = data_values[valid_mask]

        # Plot points if there are two columns
        if len(data_values.columns) == 2:
            ax.scatter(data_values[data_values.columns[0]], ts_values, data_values[data_values.columns[1]],
                       c=[color_dict[color_name]], label=legend_labels[color_name])

# Set labels and legend
ax.set_title('Touch events coordinate distribution over time')
ax.set_xlabel('X-coordinate')
ax.set_ylabel('Y-coordinate')
ax.set_zlabel('Timestamp [ms]')

# Remove duplicate labels in the legend
handles, labels = ax.get_legend_handles_labels()
unique_labels = dict(zip(labels, handles))
ax.legend(unique_labels.values(), unique_labels.keys(), title="Color", bbox_to_anchor=(1.05, 1), loc='upper left')  # Move legend to the side

# Rotate the plot
ax.view_init(elev=0, azim=-90)

plt.show()
