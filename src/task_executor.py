from src.datagen import install_and_run_datagen
from src.markdown_formatter import format_markdown
from src.date_utils import count_wednesdays
from src.contact_sorter import sort_contacts
from src.log_handler import get_recent_logs
from src.markdown_extractor import extract_markdown_titles
from src.email_processor import process_email_extraction
from src.credit_card_extractor import process_credit_card_extraction
from src.comment_analyzer import find_similar_comments_task
from src.ticket_sales import calculate_gold_ticket_sales

def execute_task(task_name):
    """Executes the specified task and returns result tuple (response_dict, status_code)"""
    task_map = {
        "install and run datagen": install_and_run_datagen,
        "format markdown": format_markdown,
        "count wednesdays": count_wednesdays,
        "sort contacts": sort_contacts,
        "recent log files": get_recent_logs,
        "extract h1 titles": extract_markdown_titles,
        "extract sender's email": process_email_extraction,
        "extract credit card": process_credit_card_extraction,
        "find similar comments": find_similar_comments_task,
        "calculate gold ticket sales": calculate_gold_ticket_sales
    }
    
    if task_name not in task_map:
        return {"error": f"Invalid task name: {task_name}"}, 400
        
    try:
        return task_map[task_name]()
    except Exception as e:
        return {"error": f"Error executing {task_name}: {str(e)}"}, 500
