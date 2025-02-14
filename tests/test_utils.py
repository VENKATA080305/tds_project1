import pytest
import sqlite3
from src.utils import count_wednesdays, sort_contacts, extract_h1_titles, execute_sql

def test_count_wednesdays():
    dates = ["2025-02-05", "2025-02-12", "2025-02-19", "2025-02-26", "2025-02-28"]
    assert count_wednesdays(dates) == 4  # 4 Wednesdays in the list

def test_sort_contacts():
    contacts = [
        {"first_name": "John", "last_name": "Doe"},
        {"first_name": "Alice", "last_name": "Smith"},
        {"first_name": "Bob", "last_name": "Doe"}
    ]
    expected_output = [
        {"first_name": "Bob", "last_name": "Doe"},
        {"first_name": "John", "last_name": "Doe"},
        {"first_name": "Alice", "last_name": "Smith"}
    ]
    assert sort_contacts(contacts) == expected_output

def test_extract_h1_titles():
    md_files = {
        "README.md": "# Home\n## Introduction",
        "models.md": "# Large Language Models\nContent",
        "empty.md": "No headers here"
    }
    expected_output = {
        "README.md": "Home",
        "models.md": "Large Language Models"
    }
    assert extract_h1_titles(md_files) == expected_output

def test_execute_sql():
    # Create an in-memory SQLite database
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE tickets (type TEXT, price INTEGER, units INTEGER)")
    cursor.execute("INSERT INTO tickets VALUES ('Gold', 100, 2)")
    cursor.execute("INSERT INTO tickets VALUES ('Gold', 150, 1)")
    cursor.execute("INSERT INTO tickets VALUES ('Silver', 50, 4)")
    conn.commit()
    
    result = execute_sql(conn, "SELECT SUM(units * price) FROM tickets WHERE type='Gold'")
    assert result == 350  # (100*2) + (150*1) = 350
    conn.close()
