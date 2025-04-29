
from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]
    filepath = os.path.join("uploads", file.filename)
    os.makedirs("uploads", exist_ok=True)
    file.save(filepath)
    
    try:
        result = subprocess.check_output(["python3", "model.py", filepath], cwd="python")
        return result.decode("utf-8")
    except subprocess.CalledProcessError as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(debug=True)
