# 🚀 Automation Agent

This project implements an automation agent API using Flask. It allows users to execute tasks and read file contents via two API endpoints:

- **POST `/run?task=<task description>`**: Executes a plain-English task using the agent.
- **GET `/read?path=<file path>`**: Returns the content of a specified file.

## ![Automation Agent](C:\Users\shivu\OneDrive\Desktop\tds_project1\README.md)

---

## ⚙️ Setup and Installation

### Step 1: Clone the Repository
```sh
git clone https://github.com/your-repo.git
cd your-repo
```

### Step 2: Set Up a Virtual Environment

**Windows:**
```sh
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```sh
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```sh
pip install -r requirements.txt
```

### Step 4: Run the Application
```sh
pytest tests/test_task_executor.py
```

---

## 🛠️ Running Instructions for Task A
To execute specific tasks, the following modules handle different operations:

| Task | Description | Module |
|------|-------------|----------|
| A1 | Install `uv` (if needed) and run `datagen.py` | `datagen.py` |
| A2 | Format Markdown content | `markdown_formatter.py` |
| A3 | Count Wednesdays in a file | `date_utils.py` |
| A4 | Sort contacts | `contact_sorter.py` |
| A5 | Extract first line from recent logs | `log_handler.py` |
| A6 | Extract H1 titles from Markdown files | `markdown_extractor.py` |
| A7 | Extract sender email from a file | `email_processor.py` |
| A8 | Extract credit card number from an image using LLM | `credit_card_extractor.py` |
| A9 | Find similar comments using embeddings | `comment_analyzer.py` |
| A10 | Calculate total sales for "Gold" tickets in an SQLite database | `ticket_sales.py` |

Additional utility files:
- `file_handler.py`: Handles file I/O operations.
- `llm_processor.py`: Implements LLM-related functions.
- `task_executor.py`: Main task execution logic.
- `utils.py`: General utility functions.

---

## 📌 Notes
- Ensure all dependencies are installed before running the application.
- You can replace `image_url_here` with an actual image URL to include visuals in the README.
- To build and deploy the project using Docker, see `Dockerfile` instructions.

---

### 📢 Contributing
Feel free to submit pull requests or report issues in the repository!

---

### 📜 License
This project is licensed under the MIT License.

