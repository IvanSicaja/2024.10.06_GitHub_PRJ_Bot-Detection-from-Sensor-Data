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
timestamp_columns = [col for col in data.columns if col.startswith("j_eT_timestamp")]
data_columns = [col for col in data.columns if col.startswith("j_eT_event_data")]
event_type_columns = [col for col in data.columns if col.startswith("j_eT_event_type")]
color_column = "color"
source_file_column = "source_file"

# Get unique colors
unique_colors = data[color_column].unique()

# Define a colormap with distinct colors for each unique color entry
cmap = plt.get_cmap('tab10')
color_dict = {color_name: cmap(i) for i, color_name in enumerate(unique_colors)}

# Map each color to its corresponding source file
source_files = {color_name: data.loc[data[color_column] == color_name, source_file_column].iloc[0] for color_name in
                unique_colors}
legend_labels = {color_name: f"{color_name} - {source_files[color_name]}" for color_name in unique_colors}

# Create the main application window
root = tk.Tk()
root.title("Developed by Ivan Sicaja © 2024")
root.geometry("350x230")  # Adjusted size for the tkinter window

# Variables to hold checkbox states
var_36 = IntVar(value=0)
var_37 = IntVar(value=0)
var_38 = IntVar(value=0)

# Global variables to store rotation values
current_elevation = 0
current_azimuth = 0

# List to store references to created figures and axes
figures_axes = []


# Function to create a new plot
def create_plot(event_types):
    fig = plt.figure(figsize=(8, 5))  # Adjusted figure size
    ax = fig.add_subplot(111, projection='3d')
    figures_axes.append((fig, ax))

    ax.clear()
    # Plotting all data points
    for color_name in unique_colors:
        color_mask = data[color_column] == color_name

        for ts_col, data_col, event_type_col in zip(timestamp_columns, data_columns, event_type_columns):
            ts_values = data.loc[color_mask, ts_col]
            data_values = data.loc[color_mask, data_col].str.split(',', expand=True)
            event_type_values = data.loc[color_mask, event_type_col]

            # Convert data values to numeric
            data_values = data_values.apply(pd.to_numeric, errors='coerce')

            # Filter out NaN values and empty event_type cells
            valid_mask = data_values.notna().all(axis=1) & event_type_values.notna()
            ts_values = ts_values[valid_mask]
            data_values = data_values[valid_mask]
            event_type_values = event_type_values[valid_mask]

            # Apply event_type filter if specified
            event_type_mask = event_type_values.isin(event_types)
            ts_values = ts_values[event_type_mask]
            data_values = data_values[event_type_mask]
            event_type_values = event_type_values[event_type_mask]

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
    legend = ax.legend(unique_labels.values(), unique_labels.keys(), title="Legend", bbox_to_anchor=(1.05, 1),
                       loc='upper left', fontsize='small')  # Move legend to the side

    # Add event type legend entries
    checkbox_labels = {
        36: '36 - Press Down Event',
        37: '37 - Move Event',
        38: '38 - Press Up Event'
    }
    checkbox_states = [checkbox_labels[event_type] for event_type in event_types]

    # Create custom legend for checkbox states
    checkbox_legend = ax.legend(
        [plt.Line2D([0], [0], color='none', marker='None', linestyle='None') for _ in checkbox_states],
        checkbox_states, loc='center left', bbox_to_anchor=(1.05, 0.5), title="Displayed events:", fontsize='small'
    )

    # Add both legends to the plot
    ax.add_artist(legend)
    ax.add_artist(checkbox_legend)

    # Rotate the plot
    ax.view_init(elev=current_elevation, azim=current_azimuth)

    plt.show()



# Checkboxes and their labels
checkbox_36 = Checkbutton(root, text="36 - Press Down Event", variable=var_36)
checkbox_37 = Checkbutton(root, text="37 - Move Event", variable=var_37)
checkbox_38 = Checkbutton(root, text="38 - Press Up Event", variable=var_38)

checkbox_36.pack(anchor='w')
checkbox_37.pack(anchor='w')
checkbox_38.pack(anchor='w')

# Function to trigger plotting with selected event types
def on_plot_button_click():
    selected_events = []
    if var_36.get() == 1:
        selected_events.append(36)
    if var_37.get() == 1:
        selected_events.append(37)
    if var_38.get() == 1:
        selected_events.append(38)

    if not selected_events:
        return  # Do nothing if no events are selected

    create_plot(selected_events)

# Button to plot the data
plot_button = Button(root, text="Plot Data", command=on_plot_button_click)
plot_button.pack()

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


# Variables to hold manual input for rotation degrees
elevation_degree_var = StringVar()
azimuth_degree_var = StringVar()

# Create Entry widgets for manual input of rotation degrees
elevation_entry = Entry(root, textvariable=elevation_degree_var)
azimuth_entry = Entry(root, textvariable=azimuth_degree_var)

elevation_label = Label(root, text="Elevation (degrees):")
azimuth_label = Label(root, text="Azimuth (degrees):")

elevation_label.pack(anchor='w')
elevation_entry.pack(anchor='w')
azimuth_label.pack(anchor='w')
azimuth_entry.pack(anchor='w')

# Buttons to apply rotation
rotation_button = Button(root, text="Apply Rotation", command=update_rotation)
rotation_button.pack()


# Main loop to run the application
root.mainloop()

