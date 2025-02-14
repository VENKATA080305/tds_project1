import pytest
import os
from unittest.mock import patch
from src.log_handler import get_recent_logs

@pytest.fixture
def mock_list_files():
    """Mock list_files to return fake log files."""
    with patch("src.log_handler.list_files") as mock_list:
        mock_list.return_value = [f"/data/logs/log{i}.log" for i in range(1, 6)]
        yield mock_list

@pytest.fixture
def mock_read_file():
    """Mock read_file to return fake log content."""
    with patch("src.log_handler.read_file") as mock_read:
        mock_read.side_effect = lambda f: f"Log entry from {f}"
        yield mock_read

@pytest.fixture
def mock_write_file():
    """Mock write_file to avoid real file writing."""
    with patch("src.log_handler.write_file") as mock_write:
        yield mock_write

@pytest.fixture
def mock_os_path_exists():
    """Mock os.path.exists to always return True."""
    with patch("os.path.exists", return_value=True):
        yield

@pytest.fixture
def mock_os_path_getmtime():
    """Mock os.path.getmtime to simulate sorting of files by modification time."""
    with patch("os.path.getmtime") as mock_mtime:
        mock_mtime.side_effect = lambda f: int(f[-5])  # Simulated timestamps
        yield mock_mtime
        
def test_get_recent_logs(mock_list_files, mock_read_file, mock_write_file, mock_os_path_exists, mock_os_path_getmtime):
    """Test get_recent_logs function."""
    response, status_code = get_recent_logs()

    assert status_code == 200
    assert response["status"] == "Recent log lines extracted"

    # Ensure write_file was called with the correct file path and the correct order
    mock_write_file.assert_called_once_with(
        "/data/logs-recent.txt",
        "\n".join([f"Log entry from /data/logs/log{i}.log" for i in range(5, 0, -1)]),  # Reverse order
    )

