import markdown2
from .file_handler import read_file, write_file

def format_markdown():
    """Formats a markdown file into HTML"""
    try:
        content = read_file("/data/input.md")
        html = markdown2.markdown(content)
        write_file("/data/output.html", html)
        return {"status": "Markdown formatted"}, 200
    except Exception as e:
        return {"error": f"Failed to format markdown: {str(e)}"}, 500
