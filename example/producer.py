#!/usr/bin/env python
import sys
from time import sleep
from json import dumps
from kafka import KafkaProducer

def produce(port):
    hostname="localhost:%d" % port
    producer = KafkaProducer(
        bootstrap_servers=[hostname],
        value_serializer=lambda x: dumps(x).encode('utf-8')
    )
    for j in range(9999):
        print("Iteration", j)
        data = {'counter': j}
        producer.send('events', value=data)
        sleep(0.5)

if __name__ == "__main__":
    port = 9092
    if len(sys.argv) == 2:
        port = int(sys.argv[1])
    produce(port)
