#!/usr/bin/env python3
import sys
from kafka import KafkaProducer

message = ' '.join(sys.argv[1:]) or "Hello!"

producer = KafkaProducer(bootstrap_servers='localhost:9092')

producer.send('my_topic', value=message.encode())
producer.flush()
print('Message sent.')

producer.close()
