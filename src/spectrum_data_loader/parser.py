import pandas as pd
from typing import List, Tuple, Optional

# 1. La función base "privada" (nota el guion bajo al inicio del nombre)
# Esta función no está pensada para ser usada directamente por el usuario final.
def _parse_file_to_lists(
    filepath: str,
    encodings: List[str],
    delimiters: List[str]
) -> Tuple[List[float], List[float]]:
    """Función interna para leer y parsear un archivo de texto a dos listas."""
    
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
        raise FileNotFoundError(f"Error: El archivo no se encontró en: {filepath}")

    if lines is None:
        raise ValueError(f"No se pudo leer el archivo '{filepath}' con las codificaciones: {encodings}")

    # Función interna para detectar el delimitador (sin cambios)
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

    sample = [line for line in lines if line.strip()][:10]
    delimiter = detect_delimiter(sample)

    if delimiter is None:
        raise ValueError("No se pudo determinar un delimitador válido en el archivo.")

    x_data: List[float] = []
    y_data: List[float] = []

    for line in lines:
        if not line.strip(): continue
        try:
            parts = [part for part in line.strip().split(delimiter) if part]
            if len(parts) >= 2:
                x_val = float(parts[0].replace(',', '.'))
                y_val = float(parts[1].replace(',', '.'))
                x_data.append(x_val)
                y_data.append(y_val)
        except (ValueError, IndexError):
            continue

    if not x_data:
        raise ValueError("No se encontraron datos numéricos válidos en el archivo.")
    
    return x_data, y_data

# 2. Tu primera función pública: carga los datos como listas.
def load_xy_data(
    filepath: str,
    encodings: List[str] = ['utf-8', 'latin-1', 'cp1252'],
    delimiters: List[str] = ['\t', ' ', '  ']
) -> Tuple[List[float], List[float]]:
    """
    Carga datos de dos columnas desde un archivo de texto y los devuelve como dos listas.

    Ideal para usar con librerías que requieren listas de datos por ejes, como Manim.
    
    Args:
        filepath (str): La ruta al archivo de texto.
        encodings (List[str], optional): Lista de codificaciones a probar.
        delimiters (List[str], optional): Lista de delimitadores a probar.

    Returns:
        Tuple[List[float], List[float]]: Una tupla con (lista_x, lista_y).
    """
    # Simplemente llama a la función base y devuelve su resultado.
    return _parse_file_to_lists(filepath, encodings, delimiters)

# 3. Tu segunda función pública: carga los datos como un DataFrame.
def load_df_data(
    filepath: str,
    column_names: Tuple[str, str] = ('x_values', 'y_values'),
    encodings: List[str] = ['utf-8', 'latin-1', 'cp1252'],
    delimiters: List[str] = ['\t', ' ', '  ']
) -> pd.DataFrame:
    """
    Carga datos de dos columnas desde un archivo y los devuelve como un DataFrame de Pandas.

    Perfecto para análisis de datos y visualización con Matplotlib, Seaborn, etc.
    
    Args:
        filepath (str): La ruta al archivo de texto.
        column_names (Tuple[str, str], optional): Nombres para las columnas del DataFrame.
        encodings (List[str], optional): Lista de codificaciones a probar.
        delimiters (List[str], optional): Lista de delimitadores a probar.

    Returns:
        pd.DataFrame: Un DataFrame de Pandas con los datos cargados.
    """
    # Llama a la función base para obtener las listas.
    x_data, y_data = _parse_file_to_lists(filepath, encodings, delimiters)
    
    # Construye y devuelve el DataFrame.
    df = pd.DataFrame({
        column_names[0]: x_data,
        column_names[1]: y_data
    })
    return df