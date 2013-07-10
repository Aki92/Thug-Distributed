import ThugD.geolocation as geolocation
from ThugD.thug_instances import thug
from celery import group

obj = geolocation.FindLocation()
country = obj.find_country()

# Running single task & getting result back
res = thug.delay(5).get()
print(res)

# Running 10 tasks in default queue & getting their results back
res = group(thug.s(t) for t in xrange(10))().get()
print(res)

# Running 5 tasks in geolocation based queue & getting their results back
res = group(thug.apply_async(args=(t,),queue='IN').get() for t in xrange(10))
print(res)

# Running 5 tasks in geolocation based queue & getting their results back
res = group(thug.apply_async(args=(t,),queue='NL').get() for t in xrange(10))
print(res)

