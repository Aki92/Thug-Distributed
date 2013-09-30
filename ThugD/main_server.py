from __future__ import absolute_import
import ThugD.geolocation as geolocation
from kombu import Queue, Exchange
import ThugD.celeryconfig
from celery import Celery

# Creating Celery Instance
thugd = Celery('ThugD.main_server', include=['ThugD.thug_instances'])

# Using settings from configuration module
thugd.config_from_object('ThugD.celeryconfig')

class GeolocationQueueConfig(object):
    """ GeolocationQueueConfig class to update Queue settings """
    def __init__(self):
        """ Finding country and running required functions """
        obj  = geolocation.FindLocation()
        self.country  = obj.find_country()
        self.update_queue()
    
    def update_queue(self):
        """ Updating Queue settings """
        country = self.country
        if(country != ''):
            thugd.conf.CELERY_QUEUES = (Queue(country, 
                                        Exchange('geo', type='direct',
                                        durable=True),
                                        binding='geo.%s'%country,
                                        routing_key='geo.%s'%country,
                                        durable=True),
                                        
                                        Queue('generic', 
                                        Exchange('generic', type='direct',
                                        durable=True),
                                        binding='generic',
                                        routing_key='generic',
                                        durable=True),
                                        )
# Running Class init function                                        
GeolocationQueueConfig()

if __name__ == '__main__':
    thugd.start()
