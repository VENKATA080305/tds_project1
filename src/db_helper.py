import sqlite3
import duckdb

def run_sqlite_query(db_path, query):
    """Execute SQL queries on SQLite."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results

def run_duckdb_query(db_path, query):
    """Execute SQL queries on DuckDB."""
    conn = duckdb.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results
