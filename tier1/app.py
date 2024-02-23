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
        heartbeat=600,
        blocked_connection_timeout=300,
    )
  )
QCHAN = QCONN.channel()

def do_tier2():
    print("this is some important log that is to help troubleshoot when an app goes bad")
    print("calling tier1 function")
    resp = requests.get("http://tier2:8080")
    return resp.text

def do_tier2_fast():
    print("called fast function")
    return f"tier 1 fast :: {do_tier2()}"

def do_tier2_slow():
    print("called slow function")
    time.sleep(1.5)
    return f"tier 1 slow :: {do_tier2()}"

def do_queue(ctx):
    print(f"this is some important log that is used to gain insight to how well we are doing registering new members")
    print(f"called queue function w/ {ctx}")
    num = random.random()
    new_num = num * 100
    if new_num > 95:
        time.sleep(1.5)
    QCHAN.queue_declare(queue="test")
    QCHAN.basic_publish(
        exchange="",
        routing_key="test",
        body=f"{ctx} {time.time()}"
    )

def do_saas(ctx):
    print(f"this is some important log that is used to determine how much we are using this external SaaS")
    print(f"called saas function w/ {ctx}")
    num = random.random()
    new_num = num * 100
    if new_num > 95:
        time.sleep(1.5)
    resp = requests.get("https://www.githubstatus.com/api/v2/summary.json")
    resp.json()

@app.route("/fast")
def fast():
    do_queue("fast")
    do_saas("fast")
    result = do_tier2_fast()
    return result

@app.route("/slow")
def slow():
    do_queue("slow")
    do_saas("slow")
    result = do_tier2_slow()
    return result
