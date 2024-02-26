from flask import Flask
import time
import sys
from mysql.connector import connect

app = Flask(__name__)

DB = connect(host="db",
             user="test",
             password="test",
             db="test",
            )

def logit(msg):
    print(f"TIER2: {msg}", file=sys.stderr)

def query_db():
    logit(f"this is some important log that is used to udpate product owners that a event was successful")
    logit("queried DB")
    with DB.cursor() as cursor:
        cursor.execute("SELECT * FROM test")
        cursor.fetchall()

@app.route("/")
def default():
    query_db()
    return f"tier 2 {time.time()}"
