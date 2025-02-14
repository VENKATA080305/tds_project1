import pytest
from unittest.mock import patch
from src.task_executor import execute_task

# Mock the entire module path for each function
@pytest.fixture(autouse=True)
def mock_dependencies():
    with patch('src.task_executor.install_and_run_datagen') as mock_datagen, \
         patch('src.task_executor.format_markdown') as mock_markdown, \
         patch('src.task_executor.count_wednesdays') as mock_count, \
         patch('src.task_executor.sort_contacts') as mock_sort, \
         patch('src.task_executor.get_recent_logs') as mock_logs, \
         patch('src.task_executor.extract_markdown_titles') as mock_titles, \
         patch('src.task_executor.process_email_extraction') as mock_email, \
         patch('src.task_executor.process_credit_card_extraction') as mock_card, \
         patch('src.task_executor.find_similar_comments_task') as mock_comments, \
         patch('src.task_executor.calculate_gold_ticket_sales') as mock_sales:
        
        # Set default return values for all mocks
        default_return = ({"status": "success"}, 200)
        mock_datagen.return_value = ({"status": "Data generated successfully"}, 200)
        mock_markdown.return_value = ({"status": "Markdown formatted"}, 200)
        mock_count.return_value = ({"status": "5 Wednesdays counted"}, 200)
        mock_sort.return_value = ({"status": "Contacts sorted"}, 200)
        mock_logs.return_value = ({"status": "Recent log lines extracted"}, 200)
        mock_titles.return_value = ({"status": "Markdown titles indexed"}, 200)
        mock_email.return_value = ({"status": "Email extracted"}, 200)
        mock_card.return_value = ({"status": "Credit card extracted"}, 200)
        mock_comments.return_value = ({"status": "Most similar comments identified"}, 200)
        mock_sales.return_value = ({"status": "Gold ticket sales calculated"}, 200)
        
        yield {
            'datagen': mock_datagen,
            'markdown': mock_markdown,
            'count': mock_count,
            'sort': mock_sort,
            'logs': mock_logs,
            'titles': mock_titles,
            'email': mock_email,
            'card': mock_card,
            'comments': mock_comments,
            'sales': mock_sales
        }

def test_install_and_run_datagen(mock_dependencies):
    result = execute_task("install and run datagen")
    assert result == ({"status": "Data generated successfully"}, 200)
    mock_dependencies['datagen'].assert_called_once()

def test_format_markdown(mock_dependencies):
    result = execute_task("format markdown")
    assert result == ({"status": "Markdown formatted"}, 200)
    mock_dependencies['markdown'].assert_called_once()

def test_count_wednesdays(mock_dependencies):
    result = execute_task("count wednesdays")
    assert result == ({"status": "5 Wednesdays counted"}, 200)
    mock_dependencies['count'].assert_called_once()

def test_sort_contacts(mock_dependencies):
    result = execute_task("sort contacts")
    assert result == ({"status": "Contacts sorted"}, 200)
    mock_dependencies['sort'].assert_called_once()

def test_get_recent_logs(mock_dependencies):
    result = execute_task("recent log files")
    assert result == ({"status": "Recent log lines extracted"}, 200)
    mock_dependencies['logs'].assert_called_once()

def test_extract_markdown_titles(mock_dependencies):
    result = execute_task("extract h1 titles")
    assert result == ({"status": "Markdown titles indexed"}, 200)
    mock_dependencies['titles'].assert_called_once()

def test_process_email_extraction(mock_dependencies):
    result = execute_task("extract sender's email")
    assert result == ({"status": "Email extracted"}, 200)
    mock_dependencies['email'].assert_called_once()

def test_process_credit_card_extraction(mock_dependencies):
    result = execute_task("extract credit card")
    assert result == ({"status": "Credit card extracted"}, 200)
    mock_dependencies['card'].assert_called_once()

def test_find_similar_comments_task(mock_dependencies):
    result = execute_task("find similar comments")
    assert result == ({"status": "Most similar comments identified"}, 200)
    mock_dependencies['comments'].assert_called_once()

def test_calculate_gold_ticket_sales(mock_dependencies):
    result = execute_task("calculate gold ticket sales")
    assert result == ({"status": "Gold ticket sales calculated"}, 200)
    mock_dependencies['sales'].assert_called_once()

def test_invalid_task():
    assert execute_task("invalid task") == ({"error": "Invalid task name: invalid task"}, 400)

def test_execution_error(mock_dependencies):
    mock_dependencies['count'].side_effect = Exception("Test error")
    assert execute_task("count wednesdays") == ({"error": "Error executing count wednesdays: Test error"}, 500)