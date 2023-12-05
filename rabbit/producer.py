#!/usr/bin/env python3
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "Hello!"
channel.basic_publish(exchange='messages', routing_key='', body=message)
print('Message sent.')

connection.close()
