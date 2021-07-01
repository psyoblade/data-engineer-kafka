#!/usr/bin/env python
import threading, time

from kafka import KafkaAdminClient, KafkaConsumer, KafkaProducer
from kafka.admin import NewTopic


producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('events', b"test")
producer.send('events', b"\xc2Hola, mundo!")
time.sleep(1)
producer.close()
