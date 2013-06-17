import pika
import time

'''
This is the Virtual Thug Instances which are taking
some integer(task) and will wait for that much time and
after that they send back the result with a message
of Job Done showing that they completed the alloted
work
'''
class RpcInstance(object):
    # Initializing the connection and channel
    def __init__(self):
        self.param = pika.ConnectionParameters(host='localhost')
        self.connection = pika.BlockingConnection(self.param)
        self.channel = self.connection.channel()
        self.consuming_requests()
        
    def consuming_requests(self):
        # Declaring "rpc_queue" from which requests will be consumed
        self.channel.queue_declare(queue='rpc_queue')
        # Distributing single task at a time to a client
        self.channel.basic_qos(prefetch_count=1)
        
        # Consuming requests from "rpc_queue" and calling "on_request" function
        self.channel.basic_consume(self.on_request, queue='rpc_queue')
        print " [x] Awaiting RPC requests"
        # Client start consuming messages from main queue => "rpc_queue"
        self.channel.start_consuming()
    
    # Processing request consumed from "rpc_queue"
    def on_request(self, ch, method, props, body):
        self.n = int(body)
        print " [.] Request(%d)"  % self.n
        
        # Calling Thug Function with request time to wait
        response = self.Thug(self.n)
        print response

        # Sending results back to main server
        ch.basic_publish(exchange='',
             routing_key=props.reply_to,
             properties=pika.BasicProperties(correlation_id = \
                                             props.correlation_id),
                                             body=str(response))
        ch.basic_ack(delivery_tag = method.delivery_tag)

    # Virtual thug function			
    def Thug(self, n):
        time.sleep(n)	
        return "%d Job done" % n

if __name__ == '__main__':
    rpc = RpcInstance()
