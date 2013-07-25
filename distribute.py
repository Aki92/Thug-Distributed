import ThugD.geolocation as geolocation
from ThugD.thug_instances import thug
from celery import group
from thread import *
import redis 
import time
    
results = []

def call_task(url, hostname):
    ans = thug.apply_async(args=(url,),queue='generic',exchange='generic',
                    binding='gen.%s'%hostname,
                    routing_key='gen.%s'%hostname)
    results.append(ans)
                    
class Distribute(object):
    def __init__(self, urls):
        self.tasks = urls
        self.make_connection()
    
    # Making connection to Redis Server 
    def make_connection(self):
        self.re = redis.StrictRedis(host='localhost', port=6379)
        
    # Sending performance to SORTED SET in Redis
    def read_db(self):
        # Reading performance value of best client from SORTED SET in Redis
        # As Sorted Set sorts in increasing order so reading in reverse order
        self.best_client = self.re.zrevrange('perf', start=0, num=0)
        
    def distribute_tasks(self):
        urls = self.tasks
        
        # Distributing 1 task at a time among best worker
        for url in urls:
            self.read_db()
            hostname = self.best_client
            print url, hostname[0]
            start_new_thread(call_task, (url,hostname[0],))
            # Updating client performance list at runtime
            time.sleep(1)

if __name__ == '__main__':
    dis = Distribute([i for i in xrange(10)])
    dis.distribute_tasks()
    print [res.get() for res in results]
            

'''
# Running 5 tasks in geolocation based queue & getting their results back
res = group(thug.apply_async(args=(t,),queue='IN').get() for t in xrange(10))
print(res)

# Running 5 tasks in geolocation based queue & getting their results back
res = group(thug.apply_async(args=(t,),queue='NL').get() for t in xrange(10))
print(res)
'''