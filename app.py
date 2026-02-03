from flask import Flask, request
from datetime import datetime
import os

app = Flask(__name__)

DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "visitors.txt")

# Ensure data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

@app.route("/")
def home():
    visitors = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            visitors = f.readlines()

    html = """
    <html>
    <head>
        <title>Visitor Log</title>
        <style>
            body { font-family: Arial; background: #f4f6f8; padding: 20px; }
            .container { max-width: 600px; margin: 0 auto; }
            .card { background: white; padding: 15px; margin: 10px 0; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
            .time { color: gray; font-size: 12px; }
            input { padding: 10px; width: 70%; margin-right: 10px; }
            button { padding: 10px 20px; background: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer; }
            button:hover { background: #0056b3; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Visitor Log Application</h1>
            <form action="/add" method="POST">
                <input type="text" name="name" placeholder="Visitor Name" required>
                <button type="submit">Add Visitor</button>
            </form>
            <h2>Visitor Entries</h2>
    """

    for line in visitors:
        if "|" in line:
            time, name = line.strip().split("|", 1)
            html += f"""
            <div class="card">
                <b>{name}</b>
                <div class="time">{time}</div>
            </div>
            """

    html += """
        </div>
    </body>
    </html>
    """
    return html


@app.route("/add", methods=["POST"])
def add_visitor():
    name = request.form.get("name")
    if name:
        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        with open(DATA_FILE, "a") as f:
            f.write(f"{timestamp}|{name}\n")
    return home()


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
```

**Create `requirements.txt`:**
```
Flask==3.0.0
pytest==7.4.0