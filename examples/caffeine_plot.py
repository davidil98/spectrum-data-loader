#
# --- Example: Loading and Plotting a text file (.txt) Spectrum File ---
#
# This script demonstrates how to:
#   1. Load spectral data from a .txt file using the spectrum_data_loader library.
#   2. Structure the data into a pandas DataFrame.
#   3. Plot the resulting UV-Vis spectrum using matplotlib.
# This also work with file .jdx

# --- 1. Import necessary libraries ---
# spectrum_data_loader: The core library for loading the data.
# matplotlib.pyplot: For plotting and data visualization.
# pandas: For data manipulation and structuring. A very common tool in data analysis.
# os: To handle file paths in a way that works across different operating systems.
import spectrum_data_loader as sdl
import matplotlib.pyplot as plt
import pandas as pd
import os

# --- 2. Define the data file path ---
# It's good practice to define a 'home' or 'data_folder' variable, especially
# when you plan to work with multiple files from the same directory.
# os.path.join creates a valid file path regardless of your OS (Windows, macOS, Linux).
home = os.path.join('examples', 'data')
file_path = os.path.join(home, 'caffeine_UV.txt')

# --- 3. Load the spectrum data ---
# This is the main function from the library.
# It automatically parses the .jdx file and returns two lists:
# one for the x-axis data (Wavelength) and one for the y-axis data (Absorbance).
wavelength, absorbance = sdl.load_xy_data(file_path)

# --- 4. Structure data into a pandas DataFrame ---
# While you can plot directly from the lists, using a pandas DataFrame is highly
# recommended as it makes data inspection, cleaning, and analysis much easier.
data = {
    'Wavelength': wavelength,
    'Absorbance': absorbance
}
df = pd.DataFrame(data)

# You can now easily inspect the data, for example:
# print(df.head())
# print(df.describe())

# You can also load the file to produce a DataFrame, described below:
# df = sdl.load_df_data(file_path)
# These produce the x and y values with the headers "x_values", "y_values".

# --- 5. Plot the spectrum ---
# Create a plot using matplotlib to visualize the data.
# We use the columns from our DataFrame for the x and y axes.
fig, ax = plt.subplots(figsize=(10, 7))

ax.plot(df['Wavelength'], df['Absorbance'], label='Caffeine UV-vis Spectrum')

# Add titles and labels for clarity
ax.set_title('UV-vis Spectrum of Caffeine')
ax.set_xlabel('Wavelength (nm)')
ax.set_ylabel('Absorbance (a.u.)')
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend()

# --- 6. Display the plot ---
# This command opens a window to show the generated figure.
plt.show()