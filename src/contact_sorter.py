import json
from .file_handler import read_file, write_file

def sort_contacts():
    """Sorts a list of contacts alphabetically"""
    try:
        contacts = json.loads(read_file("/data/contacts.json"))
        sorted_contacts = sorted(contacts, key=lambda x: x["name"])
        write_file("/data/sorted_contacts.json", json.dumps(sorted_contacts, indent=4))
        return {"status": "Contacts sorted"}, 200
    except Exception as e:
        return {"error": f"Failed to sort contacts: {str(e)}"}, 500
