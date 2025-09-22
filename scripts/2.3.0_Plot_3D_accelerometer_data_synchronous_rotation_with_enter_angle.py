import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from tkinter.ttk import Button, Entry, Label

# Define the file path
file_path = r"C:\Users\Sicaja\Desktop\SmartCodeACADEMY\0.0_Channel_topics\12_How_to_do_data_analyse_and_build_model_&_visialization\0_Data\1_Unzipped\1_OutputData\DataAfterScript_2.0_ManuallyCollectedAllExtractedFatures_TASK_2\DataAfterScript_2.0_numbers.xlsx"

# Load the necessary data
data = pd.read_excel(file_path)

# Extract relevant columns
data_columns = [col for col in data.columns if col.startswith("j_e52_event_data")]
color_column = "color"
source_file_column = "source_file"

# Create the main application window
root = tk.Tk()
root.title("3D Plotter")
root.geometry("400x200")

# Initialize global variables for plot
fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111, projection='3d')

# Function to create a new plot
def create_plot():
    ax.clear()
    # Plotting all data points
    for col in data_columns:
        for idx, row in data.iterrows():
            data_values = row[col]
            if isinstance(data_values, str):
                data_values = data_values.split(',')
                if len(data_values) == 3:
                    x, y, z = map(float, data_values)
                    color = row[color_column]  # Get color from corresponding column
                    ax.scatter(x, y, z, c=color, marker='o')
            elif isinstance(data_values, float):  # Handle float values
                ax.scatter(data_values, data_values, data_values, c='blue', marker='o')

    # Add legend with corresponding color and source file
    unique_colors = data[color_column].unique()
    for color in unique_colors:
        source_file = data.loc[data[color_column] == color, source_file_column].iloc[0]
        ax.scatter([], [], [], c=color, label=f"{color} - {source_file}")

    # Set labels
    ax.set_title('3D Scatter Plot')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')

    ax.legend()

    # Orient the axes
    ax.set_xlim(left=ax.get_xlim()[0], right=ax.get_xlim()[1])
    ax.set_ylim(bottom=ax.get_ylim()[0], top=ax.get_ylim()[1])
    ax.set_zlim(bottom=ax.get_zlim()[0], top=ax.get_zlim()[1])

    plt.show()

# Function to update global rotation values using manual entries
def update_rotation():
    try:
        current_elevation = float(elevation_entry.get())
        current_azimuth = float(azimuth_entry.get())
        ax.view_init(elev=current_elevation, azim=current_azimuth)
        fig.canvas.draw()
    except ValueError:
        return  # Ignore invalid inputs and keep the previous values

# Variables to hold manual input for rotation degrees
elevation_entry = Entry(root)
azimuth_entry = Entry(root)

elevation_label = Label(root, text="Elevation (degrees):")
azimuth_label = Label(root, text="Azimuth (degrees):")

elevation_label.pack()
elevation_entry.pack()
azimuth_label.pack()
azimuth_entry.pack()

# Buttons to apply rotation and create plot
rotation_button = Button(root, text="Apply Rotation", command=update_rotation)
rotation_button.pack()

plot_button = Button(root, text="Create Plot", command=create_plot)
plot_button.pack()

# Main loop to run the application
root.mainloop()
