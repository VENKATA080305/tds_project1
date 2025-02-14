import os

def read_file(file_path):
    """Reads content from a file"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(file_path, content):
    """Writes content to a file"""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(content))

def list_files(directory, extension=""):
    """Lists files in directory with optional extension filter"""
    if not os.path.exists(directory):
        return []
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(extension)]
DATA_DIR = "/data"

#TASK B1 AND B2

def is_safe_path(path):
    """Ensure the path is inside /data directory."""
    abs_path = os.path.abspath(path)
    return abs_path.startswith(DATA_DIR)


def delete_file(path):
    """Deny all delete requests (B2)."""
    raise PermissionError("Deletion of files is not allowed")