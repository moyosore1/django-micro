import pika

params = pika.URLParameters('amqps://wysnlzss:w-KhCiHGl5IjJrnoy_20gvuPBJ0Jdffs@poodle.rmq2.cloudamqp.com/wysnlzss')

# create connection
connection = pika.BlockingConnection(params)

# create channel
channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Received thisss')
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback)

print('started consuming')

channel.start_consuming()

channel.close()