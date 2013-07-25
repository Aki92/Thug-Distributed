import ThugD.geolocation as geolocation
from ThugD.thug_instances import thug
from celery import group, subtask

#Running single task & getting result back
res = thug.delay(5).get()
print(res)

#Running 10 tasks in default queue & getting their results back
res = group(thug.subtask(args=(t,)) for t in xrange(20))
print res().join()

# Running 5 tasks in geolocation based queue & getting their results back
res = group(thug.subtask(args=(t,), queue='IN') for t in xrange(10))
print res().join()

# Running 5 tasks in geolocation based queue & getting their results back
res = group(thug.subtask(args=(t,),queue='NL') for t in xrange(10))
print res().join()

# Running 5 tasks in geolocation based queue & getting their results back
res = group(thug.subtask(args=(t,),queue='IT') for t in xrange(10))
print res().join()

# Running 5 tasks in geolocation based queue & getting their results back
res = group(thug.subtask(args=(t,),queue='US') for t in xrange(10))
print res().join()
