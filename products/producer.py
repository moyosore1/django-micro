import json

import pika

params = pika.URLParameters('amqps://wysnlzss:w-KhCiHGl5IjJrnoy_20gvuPBJ0Jdffs@poodle.rmq2.cloudamqp.com/wysnlzss')

# create connection
connection = pika.BlockingConnection(params)

# create channel
channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)