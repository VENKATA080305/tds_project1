import re
from .file_handler import read_file, write_file

def process_email_extraction():
    """Extracts sender's email from an email text file"""
    try:
        content = read_file("/data/email.txt")
        match = re.search(r"From:\s*([\w\.-]+@[\w\.-]+)", content)
        if not match:
            return {"error": "Failed to extract email"}, 500
        
        sender_email = match.group(1)
        write_file("/data/email-sender.txt", sender_email)
        return {"status": "Email extracted"}, 200
    except Exception as e:
        return {"error": f"Failed to extract email: {str(e)}"}, 500
