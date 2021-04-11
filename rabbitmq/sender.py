import pika

credentials = pika.PlainCredentials('guest', 'guest')

# connection = pika.BlockingConnection(pika.ConnectionParameters('138.68.189.32',5672,'/',credentials))
connection = pika.BaseConnection(pika.ConnectionParameters('localhost',5672,'/',credentials))
channel = connection.channel()

channel.queue_declare(queue='duka-inv-queue')

def send_log_to_queue(message: str):
    channel.basic_publish(
        exchange='',
        routing_key='duka-inv-queue',
        body=message
    )

print(" [x] Sent 'Hello World!'")
