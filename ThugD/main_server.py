from __future__ import absolute_import
import ThugD.geolocation as geolocation
from kombu import Queue, Exchange
import ThugD.celeryconfig
from celery import Celery
from thread import *
import psutil
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

    def update_queue(self):
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

def find_performance():
    """ Finding performance of system using system config """
    nc = psutil.NUM_CPUS
    #bt = psutil.get_boot_time()
    cp = psutil.cpu_percent(interval = 1)
    fm = psutil.virtual_memory().free
    # Using simple formula: Num_Cpu*(Free_Memory(GB)*10)*(Free_Cpu/10)
    perf = nc * (fm/10**9)*10 * (100 - cp)/5
    return perf

def update_premul():
    """
    Updates the Prefetch Multiplier Setting according to System Performance
    """
    while True:
        perf = find_performance()
        pm = 0
        # Defining ranges for setting prefetch multiplier setting
        if perf < 500:
            pm = 5
        elif 500 <= perf <1000:
            pm = 10
        elif 1000 <= perf <2000:
            pm = 15
        elif 2000 <= perf <3000:
            pm = 20
        elif 3000 <= perf <3500:
            pm = 25
        elif 3500 <= perf <4000:
            pm = 30
        elif 4000 <= perf:
            pm = 40

        thugd.conf.CELERYD_PREFETCH_MULTIPLIER = pm
        # Waiting for 2 min.
        time.sleep(10)

# Running above made class
GeolocationQueueConfig()
# Starting new thread for updating prefetch multiplier setting regularly
start_new_thread(update_premul,())

if __name__ == '__main__':
    thugd.start()
