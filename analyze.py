import pandas as pd

def analyze_csv(file_path):
    """
    Analyzes a CSV file using pandas and prints the number of rows and columns.

    :param file_path: Path to the CSV file
    """
    try:
        df = pd.read_csv(file_path)
        num_rows, num_columns = df.shape
        print(f"Number of rows: {num_rows}")
        print(f"Number of columns: {num_columns}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

