import os
import requests
from flask import Flask

app = Flask(__name__)

# Week 1: this variable must be provided by the operating system.
DB_URL = os.environ["DATABASE_URL"]


@app.route("/")
def index():
    html = f"""
    <!DOCTYPE html>
    <html>
      <head>
        <title>PawsSwipe</title>
      </head>
      <body>
<h1>🐶🐱 Welcome to PawsSwipe PRO: Dogs & Cats [SECURED by ameni] 🔒</h1>
        <p>System Status: Connected to Database at [{DB_URL}]</p>
      </body>
    </html>
    """
    return html


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
