from .file_handler import read_file, write_file

def get_recent_logs():
    """Extracts last 10 lines from a log file"""
    try:
        content = read_file("/data/logs.txt").strip().split("\n")
        last_10_logs = "\n".join(content[-10:])
        write_file("/data/recent_logs.txt", last_10_logs)
        return {"status": "Recent log lines extracted"}, 200
    except Exception as e:
        return {"error": f"Failed to extract logs: {str(e)}"}, 500
