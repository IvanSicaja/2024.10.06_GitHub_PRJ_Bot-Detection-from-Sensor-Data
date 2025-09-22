import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from tkinter import IntVar, StringVar
from tkinter.ttk import Checkbutton, Button, Entry, Label

# Define the file path
file_path = r"C:\Users\Sicaja\Desktop\SmartCodeACADEMY\0.0_Channel_topics\12_How_to_do_data_analyse_and_build_model_&_visialization\0_Data\1_Unzipped\1_OutputData\DataAfterScript_2.0_ManuallyCollectedAllExtractedFatures_TASK_2\DataAfterScript_2.0_numbers.xlsx"

# Load the necessary data
data = pd.read_excel(file_path)

# Extract relevant columns
data_columns = [col for col in data.columns if col.startswith("j_e54_event_data")]
color_column = "color"
source_column = "source_file"

# Get unique colors
unique_colors = data[color_column].unique()

# Define a colormap with distinct colors for each unique color entry
cmap = plt.get_cmap('tab10')
color_dict = {color_name: cmap(i) for i, color_name in enumerate(unique_colors)}

# Create the main application window
root = tk.Tk()
root.title("Developed by Ivan Sicaja © 2024")
root.geometry("350x330")  # Adjusted size for the tkinter window

# Variables to hold checkbox states
checkbox_vars = {color: IntVar(value=0) for color in unique_colors}

# Global variables to store rotation values
current_elevation = 0
current_azimuth = 0

# List to store references to created figures and axes
figures_axes = []

# Function to create a new plot
def create_plot():
    fig = plt.figure(figsize=(8, 5))  # Adjusted figure size
    ax = fig.add_subplot(111, projection='3d')
    figures_axes.append((fig, ax))

    ax.clear()
    # Plotting all data points
    for color_name in unique_colors:
        if checkbox_vars[color_name].get() == 1:
            color_mask = data[color_column] == color_name
            source_files = data.loc[color_mask, source_column].unique()

            for data_col in data_columns:
                data_values = data.loc[color_mask, data_col].str.split(',', expand=True)

                # Convert data values to numeric
                data_values = data_values.apply(pd.to_numeric, errors='coerce')

                # Plot points if there are three columns
                if len(data_values.columns) == 3:
                    ax.scatter(data_values[data_values.columns[0]],
                               data_values[data_values.columns[1]],
                               data_values[data_values.columns[2]],
                               c=[color_dict[color_name]], label=f"{color_name} - {', '.join(source_files)}", alpha=1.0)

    # Set labels and legend
    ax.set_title('Gyroscope 3D coordinates plot')
    ax.set_xlabel('X-coordinate')
    ax.set_ylabel('Y-coordinate')
    ax.set_zlabel('Z-coordinate')

    # Remove duplicate labels in the legend
    handles, labels = ax.get_legend_handles_labels()
    unique_labels = dict(zip(labels, handles))
    legend = ax.legend(unique_labels.values(), unique_labels.keys(), title="Legend", bbox_to_anchor=(1.05, 1),
                       loc='upper left', fontsize='small')  # Move legend to the side

    plt.show()

# Function to update global rotation values using manual entries
def update_rotation():
    global current_elevation, current_azimuth
    try:
        current_elevation = int(elevation_degree_var.get())
        current_azimuth = int(azimuth_degree_var.get())
    except ValueError:
        return  # Ignore invalid inputs and keep the previous values

    for fig, ax in figures_axes:
        ax.view_init(elev=current_elevation, azim=current_azimuth)
        fig.canvas.draw()

# Checkboxes and their labels
checkboxes = {}
for color_name in unique_colors:
    checkboxes[color_name] = Checkbutton(root, text=f"{color_name}", variable=checkbox_vars[color_name])
    checkboxes[color_name].pack(anchor='w')

# Button to plot the data
plot_button = Button(root, text="Create Plot", command=create_plot)
plot_button.pack()

# Variables to hold manual input for rotation degrees
elevation_degree_var = StringVar()
azimuth_degree_var = StringVar()

# Create Entry widgets for manual input of rotation degrees
elevation_label = Label(root, text="Elevation (degrees):")
elevation_label.pack(anchor='w')
elevation_entry = Entry(root, textvariable=elevation_degree_var)
elevation_entry.pack(anchor='w')

azimuth_label = Label(root, text="Azimuth (degrees):")
azimuth_label.pack(anchor='w')
azimuth_entry = Entry(root, textvariable=azimuth_degree_var)
azimuth_entry.pack(anchor='w')

# Button to apply rotation
rotation_button = Button(root, text="Apply Rotation", command=update_rotation)
rotation_button.pack()

# Main loop to run the application
root.mainloop()
