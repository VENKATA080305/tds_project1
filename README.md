# 🚀 Automation Agent  

This project implements an automation agent API using Flask that allows users to execute tasks and read file contents. The API exposes two endpoints:

- `/run` to execute a task based on a description.
- `/read` to read the content of a file.

## Project Structure
/app ├── app.py # Main Flask application ├── task_executor.py # Task execution logic ├── file_handler.py # File reading logic ├── Dockerfile # Docker container setup ├── requirements.txt # Python dependencies ├── README.md # Project documentation └── tests/ └── test_main.py # Tests for the API endpoints


## Setup and Installation

### 1. Clone the repository:

```bash
git clone https://github.com/your-repo.git
cd your-repo

## Set up the virtual environment

python -m venv venv


## Activate the virtual environment:


On Windows:
bash
.\venv\Scripts\Activate


On macOS/Linux:
bash
source venv/bin/activate


## Install dependencies:
bash
pip install -r requirements.txt


## Run the application:


bash
python app.py
The app will start on http://localhost:5000. You can test the /run and /read endpoints.

Running Tests
To run the tests:

bash
pytest tests/test_main.py


## Docker Support
Build the Docker Image:
bash
docker build -t automation-agent-api .


## Run the Docker Container:
bash
docker run -p 5000:5000 automation-agent-api
The Flask application will now be accessible at http://localhost:5000