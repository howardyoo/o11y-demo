from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def default():
    return f"tier 2 {time.time()}"
