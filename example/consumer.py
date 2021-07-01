from kafka import KafkaAdminClient, KafkaConsumer, KafkaProducer

consumer = KafkaConsumer(bootstrap_servers='localhost:9092', auto_offset_reset='earliest', consumer_timeout_ms=1000)
consumer.subscribe(['events'])
for message in consumer:
	print(message)
consumer.close()
