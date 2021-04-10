import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

credentials = pika.PlainCredentials('guest', 'guest')
channel.queue_declare(queue='duka-inv-queue', credentials)

def send_log_to_queue(message: str):
    channel.basic_publish(
        exchange='',
        routing_key='duka-inv-queue',
        body=message
    )

connection.close()
print(" [x] Sent 'Hello World!'")
