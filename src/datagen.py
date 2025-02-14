import os
import subprocess

def install_and_run_datagen():
    """Installs required dependencies and runs datagen.py"""
    try:
        script_path = "/data/datagen.py"
        if not os.path.exists(script_path):
            return {"error": "datagen.py not found"}, 500

        subprocess.run(["python3", script_path], check=True)
        return {"status": "Data generated successfully"}, 200
    except subprocess.CalledProcessError as e:
        return {"error": f"Failed to run datagen.py: {str(e)}"}, 500
