from flask import Flask
import time
from mysql.connector import connect, Error

app = Flask(__name__)

with connect(
    host="db",
    user="test",
    password="test"
) as DB:
    pass

def query_db():
    with DB.cursor() as cursor:
        cursor.execute("SELECT * FROM test")
        result = cursor.fetchall()

@app.route("/")
def default():
    query_db()
    return f"tier 2 {time.time()}"
