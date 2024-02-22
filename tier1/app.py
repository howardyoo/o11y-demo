from flask import Flask
import time
import requests

app = Flask(__name__)

def do_fast():
    print("called fast function")
    resp = requests.get("http://tier2:8080")
    return f"tier 1 fast :: {resp.text}"

def do_slow():
    print("called slow function")
    time.sleep(1.5)
    resp = requests.get("http://tier2:8080")
    return f"tier 1 slow :: {resp.text}"

@app.route("/fast")
def fast():
    return do_fast()

@app.route("/slow")
def slow():
    return do_slow()
