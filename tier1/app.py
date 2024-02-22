from flask import Flask
import time
import requests
import random
import pika

app = Flask(__name__)

QCREDS = pika.PlainCredentials("test","test")
QCONN = pika.BlockingConnection(
    pika.ConnectionParameters(
        host="queue",
        credentials=QCREDS,
    )
  )
QCHAN = QCONN.channel()

def do_fast():
    print("called fast function")
    resp = requests.get("http://tier2:8080")
    return f"tier 1 fast :: {resp.text}"

def do_slow():
    print("called slow function")
    time.sleep(1.5)
    resp = requests.get("http://tier2:8080")
    return f"tier 1 slow :: {resp.text}"

def do_queue(ctx):
    print("called queue function")
    num = random.random()
    new_new = num * 100
    if new_new > 90:
        time.sleep(1.5)
    QCHAN.queue_declare(queue="test")
    QCHAN.basic_publish(
        exchange="",
        routing_key="test",
        body=f"{ctx} {time.time()}"
    )

@app.route("/fast")
def fast():
    do_queue("fast")
    return do_fast()

@app.route("/slow")
def slow():
    do_queue("slow")
    return do_slow()
