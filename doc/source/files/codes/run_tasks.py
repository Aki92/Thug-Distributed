import ThugD.geolocation as geolocation
from ThugD.thug_instances import thug
from celery import group, subtask
import json

# Options to pass 
options = {'--w':10}

# JSON format of options
opts = json.dumps(options)

#Running single task & getting result back
res = thug.apply_async(args=('https://www.google.co.in/', opts, )).get()
print(res)
