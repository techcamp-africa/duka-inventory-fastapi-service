import pika

credentials = pika.PlainCredentials('duka', 'Fuckyou31')

connection = pika.BlockingConnection(pika.ConnectionParameters('138.68.189.32',15672,'/', credentials))
channel = connection.channel()

channel.queue_declare(queue='duka-inv-queue')

def send_log_to_queue(message: str):
    channel.basic_publish(
        exchange='',
        routing_key='duka-inv-queue',
        body=message
    )

print(" [x] Sent 'Hello World!'")
