import pytest
from unittest.mock import patch
from src.main import app
from unittest.mock import mock_open, patch


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@patch("src.main.execute_task")
def test_run_task_success(mock_task_executor, client):
    mock_task_executor.return_value = {"status": "success", "result": "Task executed successfully"}
    
    response = client.post("/run?task=Run%20task%20example")
    assert response.status_code == 200
    assert response.json == {"status": "success", "result": "Task executed successfully"}


@patch("src.main.execute_task")
def test_run_task_value_error(mock_task_executor, client):
    mock_task_executor.return_value = {"status": "error", "result": "Invalid task"}
    
    response = client.post("/run?task=Invalid%20task")
    assert response.status_code == 500
    assert response.json == {"status": "error", "result": "Invalid task"}


def test_read_file_success(client):
    """Mock file reading to simulate a valid file read"""
    with patch("builtins.open", mock_open(read_data="File content here")):
        response = client.get("/read?path=/path/to/file")
        assert response.status_code == 200
        assert response.json == {"status": "success", "result": "File content here"}


def test_read_file_not_found(client):
    """Test case for a missing file"""
    response = client.get("/read?path=/nonexistent/file")
    assert response.status_code == 404
    assert response.json == {"status": "error", "result": "File not found"}
