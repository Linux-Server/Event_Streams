from fastapi import FastAPI
import pika
app=FastAPI()

# Connection Establishment
connection = pika.BlockingConnection(pika.URLParameters('amqps://{username}:{password}@b-affbc5c5-8a0d-4034-bdf9-56cbc5151c63.mq.ap-south-1.amazonaws.com:5671'))
channel = connection.channel()

# Create a rabbitmq queue, otherwise message will be ddropped
channel.queue_declare(queue='hellos')

# message should always pass through an exchange

channel.basic_publish(exchange='',
                      routing_key='hellos',
                      body='Hey hddwow wecfweadcdre!')
print(" [x] Sent 'Hello World!'")


connection.close()


# @app.get('/')
# def one():
#     return "hello service one"
