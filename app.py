
from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route('/api/data')
def home():
    try:
        db = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        db.close()
        return "Application and Database connected successfully!"
    except Exception as e:
        return f"Database connection failed: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
