"""
    This program sends a message to a queue on the RabbitMQ server.

    Author: Denise Case
    Date: January 14, 2023

"""

# Eden Anderson / 1.29.23 / Hello World V1

# add imports at the beginning of the file
import pika

# create a blocking connection to the RabbitMQ server
conn = pika.BlockingConnection(pika.ConnectionParameters("LOCALHOST"))
# use the connection to create a communication channel
ch = conn.channel()
# use the channel to declare a queue
ch.queue_declare(queue="hello")
# use the channel to publish a message to the queue
#add variable for message
message = "Holy cow - I think this is working!"
ch.basic_publish(exchange="", routing_key="hello", body=message)
# print a message to the console for the user
print(f" [x] Sent {message}")
# close the connection to the server
conn.close()
