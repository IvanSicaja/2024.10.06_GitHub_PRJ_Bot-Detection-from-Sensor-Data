import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import tkinter as tk
from tkinter import ttk

# Define the file path
file_path = r"C:\Users\Sicaja\Desktop\SmartCodeACADEMY\0.0_Channel_topics\12_How_to_do_data_analyse_and_build_model_&_visialization\0_Data\1_Unzipped\1_OutputData\DataAfterScript_2.0_ManuallyCollectedAllExtractedFatures_TASK_2\DataAfterScript_2.0_numbers.xlsx"

# Load the necessary data
data = pd.read_excel(file_path)

# Extract columns dynamically
timestamp_columns = [col for col in data.columns if col.startswith("j_e57_timestamp")]
data_columns = [col for col in data.columns if col.startswith("j_e57_event_data")]
color_column = "color"
source_file_column = "source_file"

# Get unique colors and corresponding source files
unique_colors = data[color_column].unique()
color_source_file_mapping = {color: data.loc[data[color_column] == color, source_file_column].iloc[0] for color in unique_colors}

# Define a colormap with distinct colors for each unique color entry
cmap = plt.get_cmap('tab10')
colors = [cmap(i) for i in range(len(unique_colors))]  # Using tab10 for up to 10 unique colors
color_dict = {color_name: colors[i] for i, color_name in enumerate(unique_colors)}

# Function to update the plot based on selected colors
def update_plot(selected_colors):
    plt.figure(figsize=(12, 8))

    for color_name in selected_colors:
        color_mask = data[color_column] == color_name

        for ts_col, data_col in zip(timestamp_columns, data_columns):
            ts_values = data.loc[color_mask, ts_col]
            data_values = data.loc[color_mask, data_col]

            # Drop NaN values
            valid_mask = ts_values.notna() & data_values.notna()
            ts_values = ts_values[valid_mask]
            data_values = data_values[valid_mask]

            # Sort by timestamp
            sorted_indices = ts_values.argsort()
            ts_values = ts_values.iloc[sorted_indices]
            data_values = data_values.iloc[sorted_indices]

            # Plot lines connecting the points with added transparency (alpha)
            plt.plot(ts_values, data_values, color=color_dict[color_name], marker='o', linestyle='-', alpha=0.5,
                     label="" if ts_col != 'j_e57_timestamp[0000]' else None)

    # Create a custom legend for the colors
    custom_legend = [plt.Line2D([0], [0], marker='o', color=color_dict[color_name],
                                label=f"{color_name}-{color_source_file_mapping[color_name]}", markersize=10) for color_name in selected_colors]
    plt.legend(handles=custom_legend, title="Legend")

    plt.title('Pressure sensor data distribution over time')
    plt.xlabel('Timestamp [ms]')
    plt.ylabel('Pressure sensor data [hPa]')
    plt.grid(True)
    plt.show()

# Function to handle button click
def on_button_click():
    selected_colors = [color for color, var in color_vars.items() if var.get() == 1]
    update_plot(selected_colors)

# Create the main window
root = tk.Tk()
root.title("Select Colors to Display")

# Create a dictionary to hold the Tkinter variables for checkboxes
color_vars = {color: tk.IntVar(value=1) for color in unique_colors}

# Create checkboxes for each unique color
for color in unique_colors:
    chk = ttk.Checkbutton(root, text=color, variable=color_vars[color])
    chk.pack(anchor=tk.W)

# Create the button to update the plot
update_button = ttk.Button(root, text="Update Plot", command=on_button_click)
update_button.pack(anchor=tk.W, pady=10)

# Start the Tkinter event loop
root.mainloop()
