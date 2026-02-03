from flask import Flask, request, redirect
from datetime import datetime
import os

app = Flask(__name__)

# File to store visitor data
DATA_FILE = 'data/visitors.txt'

# Ensure data directory exists
os.makedirs('data', exist_ok=True)

@app.route('/')
def index():
    # Read all visitors from file
    visitors = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            for line in f:
                if line.strip():
                    visitors.append(line.strip())
    
    # Generate visitor list HTML
    visitor_html = ""
    if visitors:
        for visitor in visitors:
            visitor_html += f'<div class="visitor-item">{visitor}</div>'
    else:
        visitor_html = '<div class="no-visitors">No visitors logged yet</div>'
    
    # Return HTML directly
    html = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Visitor Log Application</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                background-color: #f4f4f4;
            }}
            .container {{
                background-color: white;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}
            h1 {{
                color: #333;
                text-align: center;
            }}
            form {{
                margin: 20px 0;
                display: flex;
                gap: 10px;
            }}
            input[type="text"] {{
                flex: 1;
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 4px;
                font-size: 16px;
            }}
            button {{
                padding: 10px 20px;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                font-size: 16px;
            }}
            button:hover {{
                background-color: #45a049;
            }}
            .visitor-list {{
                margin-top: 30px;
            }}
            .visitor-list h2 {{
                color: #333;
                border-bottom: 2px solid #4CAF50;
                padding-bottom: 10px;
            }}
            .visitor-item {{
                padding: 12px;
                margin: 10px 0;
                background-color: #f9f9f9;
                border-left: 4px solid #4CAF50;
                border-radius: 4px;
            }}
            .no-visitors {{
                text-align: center;
                color: #666;
                font-style: italic;
                padding: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🏢 Visitor Log Application</h1>
            
            <form action="/add_visitor" method="POST">
                <input type="text" name="name" placeholder="Enter visitor name" required>
                <button type="submit">Add Visitor</button>
            </form>

            <div class="visitor-list">
                <h2>Visitor Records</h2>
                {visitor_html}
            </div>
        </div>
    </body>
    </html>
    '''
    return html

@app.route('/add_visitor', methods=['POST'])
def add_visitor():
    name = request.form.get('name')
    if name:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        entry = f"{name} - {timestamp}"
        
        # Append to file
        with open(DATA_FILE, 'a') as f:
            f.write(entry + '\n')
    
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)