#!/usr/bin/env python3
import pika


def callback(ch, method, properties, body):
    print(f'Received: {body.decode()}')


connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()
channel.exchange_declare(exchange='messages', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='messages', queue=queue_name)

channel.basic_consume(
    queue=queue_name,
    on_message_callback=callback,
    auto_ack=True
)

print('Reading messages. Press Ctrl+C to exit.\n')
channel.start_consuming()
