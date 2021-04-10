import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='duka-sales-queue')

def send_log_to_queue(message: str):
    channel.basic_publish(
        exchange='',
        routing_key='duka-sales-queue',
        body=message
    )

connection.close()
print(" [x] Sent 'Hello World!'")
