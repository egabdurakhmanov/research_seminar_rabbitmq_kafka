#!/usr/bin/env python3
import sys
from kafka import KafkaConsumer

group_id = sys.argv[1] if len(sys.argv) > 1 else None

consumer = KafkaConsumer(
    bootstrap_servers='localhost:9092',
    group_id=group_id,
    auto_offset_reset='earliest'
)
consumer.subscribe(['my_topic'])

print('Reading messages. Press Ctrl+C to exit.\n')
for message in consumer:
    print(f'Received: {message.value.decode()}')

consumer.close()
