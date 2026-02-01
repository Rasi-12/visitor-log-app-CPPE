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
            body { font-family: Arial; background: #f4f6f8; }
            .card { background: white; padding: 15px; margin: 10px; border-radius: 8px; }
            .time { color: gray; font-size: 12px; }
        </style>
    </head>
    <body>
        <h1>Visitor Log Application</h1>
        <form action="/add" method="POST">
            <input type="text" name="name" placeholder="Visitor Name" required>
            <button type="submit">Add Visitor</button>
        </form>
        <h2>Visitor Entries</h2>
    """

    for line in visitors:
        time, name = line.strip().split("|", 1)
        html += f"""
        <div class="card">
            <b>{name}</b>
            <div class="time">{time}</div>
        </div>
        """

    html += "</body></html>"
    return html


@app.route("/add", methods=["POST"])
def add_visitor():
    name = request.form.get("name")
    if name:
        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        with open(DATA_FILE, "a") as f:
            f.write(f"{timestamp}|{name}\n")
    return home()


if __name__ == "__main__":
    app.run(debug=False)
