# Spectrum Data Loader

A simple and robust library for easy loading 2-column (X, Y) spectrum data from text files (.txt). The resulting data can be analyzed as DataFrame for direct plotting, or loaded as two lists for mathematical treatments and post-visualization, or plot method for other visualization modes such as Manim (as demonstrated in the examples).

The output is ready for immediate use with libraries like NumPy, Pandas, and Matplotlib for scientific analysis and visualization.

## Key Features

-   **Simple Interface**: Load any supported spectrum with a single function call: `load_xy_data()`.
-   **Versatile**: Auto-detects common delimiters like spaces, tabs, and commas.
-   **Format Support**: Works with standard text-based formats (`.txt`) and the JCAMP-DX (`.jdx`) format.
-   **Seamless Integration**: Returns data as two clean NumPy arrays, perfect for the scientific Python ecosystem (SciPy, Pandas, Matplotlib).

## Installation

```bash
pip install spectrum-data-loader
```

## Quickstart

Here is a minimal example of how to load and plot a spectrum from a text file.

```python
import spectrum_data_loader as sdl
import matplotlib.pyplot as plt

try:
    # Load the data using the library
    wavelength, absorbance = sdl.load_xy_data('my_spectrum.txt')

    # Print a confirmation
    print(f"Successfully loaded {len(wavelength)} data points.")

    # Create a simple plot with Matplotlib
    plt.figure(figsize=(8, 5))
    plt.plot(wavelength, absorbance, label='My Spectrum')
    plt.xlabel("Wavelength (nm)")
    plt.ylabel("Absorbance (a.u.)")
    plt.title("Spectrum Data")
    plt.grid(True)
    plt.legend()
    plt.show()

except FileNotFoundError:
    print("Error: The file 'my_spectrum.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
```

## Examples
For more advanced use cases, please see the code in the /examples directory of this repository.
