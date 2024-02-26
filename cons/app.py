import time
import random
import pika
import sys
import functools
from mysql.connector import connect

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
QCHAN.queue_declare(queue="test")
QCHAN.basic_qos(prefetch_count=1)

DB = connect(host="db",
             user="test",
             password="test",
             db="test",
            )

def logit(msg):
    print(f"CONSQUE: {msg}", file=sys.stderr)

def query_db():
    logit(f"this is just to note i have done something against the DB")
    logit("queried DB")
    with DB.cursor() as cursor:
        cursor.execute("SELECT * FROM test")
        cursor.fetchall()

def on_message(chan, method_frame, header_frame, body, userdata=None):
    logit(f"this is an event log just to show something important was processed")
    num = random.random()
    new_num = num * 100
    if new_num > 95:
        time.sleep(1.5)
    chan.basic_ack(delivery_tag=method_frame.delivery_tag)
    query_db()

def cons_queue():
    logit(f"called consumer setup queue function")
    on_message_callback = functools.partial(
         on_message,
         userdata="on_message_userdata"
    )
    QCHAN.basic_consume("test", on_message_callback)
    try:
        QCHAN.start_consuming()
    except KeyboardInterrupt:
        QCHAN.stop_consuming()
    logit(f"ending consumer setup queue function")
    QCONN.close()

cons_queue()
