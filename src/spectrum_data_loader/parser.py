import pandas as pd
from typing import List, Tuple, Optional

# 1. The "private" base function (note the leading underscore).
# This function is not intended to be used directly by the end-user.
def _parse_file_to_lists(
    filepath: str,
    encodings: List[str],
    delimiters: List[str]
) -> Tuple[List[float], List[float]]:
    """Internal function to read and parse a text file into two lists."""
    
    lines = None
    try:
        for encoding in encodings:
            try:
                with open(filepath, 'r', encoding=encoding) as f:
                    lines = f.readlines()
                break
            except UnicodeDecodeError:
                continue
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File not found at: {filepath}")

    if lines is None:
        raise ValueError(f"Could not read the file '{filepath}' with the provided encodings: {encodings}")

    # Internal function to detect the delimiter (no changes needed here)
    def detect_delimiter(sample_lines: List[str]) -> Optional[str]:
        for line in sample_lines:
            if not line.strip(): continue
            for sep in delimiters:
                parts = line.strip().split(sep)
                if len(parts) >= 2:
                    try:
                        float(parts[0].replace(',', '.'))
                        float(parts[1].replace(',', '.'))
                        return sep
                    except ValueError:
                        continue
        return None

    sample = [line for line in lines if line.strip()][:50]
    delimiter = detect_delimiter(sample)

    if delimiter is None:
        # Translated error message
        raise ValueError("Could not determine a valid delimiter in the file.")

    x_data: List[float] = []
    y_data: List[float] = []

    for line in lines:
        if not line.strip(): continue
        try:
            parts = [part for part in line.strip().split(delimiter) if part]
            if len(parts) == 2:
                x_val = float(parts[0].replace(',', '.'))
                y_val = float(parts[1].replace(',', '.'))
                x_data.append(x_val)
                y_data.append(y_val)
        except (ValueError, IndexError):
            continue

    if not x_data:
        raise ValueError("No valid numerical data was found in the file.")
    
    return x_data, y_data

# 2. Your first public function: loads data as lists.
def load_xy_data(
    filepath: str,
    encodings: List[str] = ['utf-8', 'latin-1', 'cp1252'],
    delimiters: List[str] = ['\t', ' ', '  ', ',']
) -> Tuple[List[float], List[float]]:
    """
    Loads two-column data from a text file and returns it as two lists.

    Ideal for use with libraries that require lists of data per axis, such as Manim.
    
    Args:
        filepath (str): The path to the text file.
        encodings (List[str], optional): A list of encodings to try.
        delimiters (List[str], optional): A list of delimiters to try.

    Returns:
        Tuple[List[float], List[float]]: A tuple containing (x_list, y_list).
    """
    # Simply calls the base function and returns its result.
    return _parse_file_to_lists(filepath, encodings, delimiters)

# 3. Your second public function: loads data as a DataFrame.
def load_df_data(
    filepath: str,
    column_names: Tuple[str, str] = ('x_values', 'y_values'),
    encodings: List[str] = ['utf-8', 'latin-1', 'cp1252'],
    delimiters: List[str] = ['\t', ' ', '  ', ',']
) -> pd.DataFrame:
    """
    Loads two-column data from a file and returns it as a pandas DataFrame.

    Args:
        filepath (str): The path to the text file.
        column_names (Tuple[str, str], optional): Names for the DataFrame columns.
        encodings (List[str], optional): A list of encodings to try.
        delimiters (List[str], optional): A list of delimiters to try.

    Returns:
        pd.DataFrame: A pandas DataFrame with the loaded data.
    """
    # Calls the base function to get the lists.
    x_data, y_data = _parse_file_to_lists(filepath, encodings, delimiters)
    
    # Builds and returns the DataFrame.
    df = pd.DataFrame({
        column_names[0]: x_data,
        column_names[1]: y_data
    })
    return df