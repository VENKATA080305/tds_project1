import os
import pytest
from src.api_fetcher import fetch_and_save
from src.git_helper import clone_and_commit
from src.db_helper import run_sqlite_query
from src.web_scraper import scrape_website
from src.image_processor import resize_image
from src.transcriber import transcribe_audio
from src.markdown_converter import convert_md_to_html
from src.csv_filter import filter_csv

@pytest.mark.skipif(os.environ.get("CI") is not None, reason="Skipping network tests in CI")
def test_fetch_and_save():
    assert "Data saved" in fetch_and_save("https://jsonplaceholder.typicode.com/posts", "/data/test.json")

def test_clone_and_commit():
    assert "Committed changes" in clone_and_commit("https://github.com/user/repo.git")

def test_run_sqlite_query():
    assert run_sqlite_query("/data/test.db", "CREATE TABLE IF NOT EXISTS test (id INTEGER)") == []

def test_scrape_website():
    assert "Example Domain" in scrape_website("https://example.com")

def test_resize_image():
    assert "Image saved" in resize_image("/data/input.jpg", "/data/output.jpg")

@pytest.mark.skip(reason="Whisper model requires manual setup")
def test_transcribe_audio():
    assert len(transcribe_audio("/data/audio.mp3")) > 0

def test_convert_md_to_html():
    assert "<h1>" in convert_md_to_html("# Test Markdown")

def test_filter_csv():
    assert "[]" in filter_csv("/data/data.csv", "status", "Active")

if __name__ == "__main__":
    pytest.main()
