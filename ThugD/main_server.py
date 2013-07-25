from __future__ import absolute_import
import ThugD.geolocation as geolocation
import ThugD.find_send_perf as fsp
from kombu import Queue, Exchange
import ThugD.celeryconfig
from celery import Celery
from thread import *
import time

# Creating Celery Instance
thugd = Celery('ThugD.main_server', include=['ThugD.thug_instances'])

# Using settings from configuration module
thugd.config_from_object('ThugD.celeryconfig')

# Making GeolocationQueueConfig class to update Queue settings
class GeolocationQueueConfig(object):
    def __init__(self):
        obj  = geolocation.FindLocation()
        self.country  = obj.find_country()
        self.update_queue()
        self.hostname = 'w1'
    
    def update_queue(self):
        country = self.country
        hostname = 'w1'
        if(country != ''):
            thugd.conf.CELERY_QUEUES = (Queue(country, 
                                        Exchange('geo', type='direct',
                                        durable=True),
                                        binding='geo.%s'%hostname,
                                        routing_key='geo.%s'%hostname,
                                        durable=True),
                                        
                                        Queue('gen.%s'%hostname, 
                                        Exchange('generic', type='direct',
                                        durable=True),
                                        binding='gen.%s'%hostname,
                                        routing_key='gen.%s'%hostname,
                                        durable=True),
                                        )
GeolocationQueueConfig()

def send_perf_value():
    fs = fsp.FindSendPerformance()
    # Updating performance value after every 2 min.
    while True:
        fs.find_performance()
        fs.send_value()
        # Waiting for 10sec.
        time.sleep(10)
        
start_new_thread(send_perf_value,())
        
if __name__ == '__main__':
    thugd.start()