import re
from .file_handler import read_file, write_file

def extract_markdown_titles():
    """Extracts H1 titles from a markdown file"""
    try:
        content = read_file("/data/input.md")
        titles = re.findall(r"^# (.+)", content, re.MULTILINE)
        write_file("/data/titles.txt", "\n".join(titles))
        return {"status": "Markdown titles indexed"}, 200
    except Exception as e:
        return {"error": f"Failed to extract markdown titles: {str(e)}"}, 500
