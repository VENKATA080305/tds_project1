import requests
import json
from src.file_handler import write_file  # Ensure this file exists and follows B1/B2

def fetch_and_save(url, save_path):
    """Fetch data from an API and securely save it inside /data."""
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        write_file(save_path, json.dumps(data, indent=2))
        return f"Data saved to {save_path}"
    else:
        return f"Error: {response.status_code}"
