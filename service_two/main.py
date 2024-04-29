from fastapi import FastAPI
import pika
app=FastAPI()

# Connection Establishment
connection = pika.BlockingConnection(pika.URLParameters('amqps://{username}:{password}@b-affbc5c5-8a0d-4034-bdf9-56cbc5151c63.mq.ap-south-1.amazonaws.com:5671'))
channel = connection.channel()

# Create a rabbitmq queue, otherwise message will be ddropped
channel.queue_declare(queue='hellos')

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")
    


channel.basic_consume(queue='hellos', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()