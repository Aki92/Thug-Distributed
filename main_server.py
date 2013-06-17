import threading
import pika
import uuid

'''
This is the Main Server where all URLs(requests) are added up
into a main queue named as "rpc_queue" and with every request
a callback queue is attached by which main server will get back
the results from clients and a unique corelation id is also
added to differentiate between different requests
'''
class RpcServer(object):
    # Initializing the connection and channel
    def __init__(self):
    	self.param = pika.ConnectionParameters(host='localhost')
        self.connection = pika.BlockingConnection(self.param)
        self.channel = self.connection.channel()
        self.response = None
        self.result_queue()

    def result_queue(self):
        # Declaring callback queue
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)
        self.corr_id = str(uuid.uuid4())
        
    def on_response(self, ch, method, props, body):
        # Checking that received msg "id" is same with request "id" send
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        # Declaring main queue in which request is being added up
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                         reply_to = self.callback_queue,
                                         correlation_id = self.corr_id,
                                         delivery_mode = 2,
                                         ),
                                   body=str(n))
        
        # Waiting till result is not received
        while self.response is None:
            self.connection.process_data_events()
            
    	print " [.] Got %r" % (self.response)

class MyThread(threading.Thread):
    # Initializing Threading instance
    def __init__(self,time):
        threading.Thread.__init__(self)
        self.time = time

    # Function that will run when start() is fired (eg. th1.start() )
    def run(self):
        rpc = RpcServer()
        print " [x] Requesting fib(%d)" % self.time
        rpc.call(self.time)
	
if __name__ == '__main__':
    # Making request threads
    th1 = MyThread(5)
    th2 = MyThread(10)
    th3 = MyThread(2)
    th4 = MyThread(7)

    # Starting threads
    th1.start()
    th2.start()
    th3.start()
    th4.start()
    
