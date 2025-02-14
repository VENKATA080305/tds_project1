import pandas as pd

def filter_csv(csv_path, column, value):
    """Filter a CSV file and return matching rows as JSON."""
    df = pd.read_csv(csv_path)
    filtered_df = df[df[column] == value]
    return filtered_df.to_json(orient="records")
