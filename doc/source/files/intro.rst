.. _intro:

*********************
Introduction to ThugD
*********************

**ThugD** as the name suggests is the **Distributed** version of project **Thug**.


Till now Thug was working as an stand-alone tool and does not provide any way to distribute URL analysis tasks to different workers. For the same reason it is neither able to analyze difference in attacks to users according to their geolocation (unless it is provided a set of differently geolocated proxies to use obviously). But now **ThugD** project is successful in solving both the problems. 


Implementations
###############

1. **Distributing URLs Automatically**:
  
**Overview**:
Here we don't consider any difference in the Capability of the clients running Thug Instances.

In it a Centralized Server is maintained which feeds URLs(collected from Spamtraps) into 2 different types of Queues(Generic & Geolocation based) according to need while on other side whenever a Thug Instance is started anywhere across the globe it automatically connects to both queues and then if the URLs are present in that queues they are automatically distributed(using Celery) to the Thug Instances. Then Thug instances processes the URLs and returns back the results to server.


2. **Distributing URLs Manually**:
  
**Overview**:
Here we were able to consider the Capability of the clients running Thug Instances at the cost of automatically distributing URLs as in it we had to distribute URLs manually.

In it a Centralized Server and a Redis Server is maintained. Thug Instances updates their System Capability on Redis Server's Sorted Set data structure after every 2 minutes so that all Clients remain in sorted order at Redis Server. 

Whenever Centralized Server wants to distribute URLs it queries Redis Server and distributes URLs to clients using Direct to Worker Queue and get back the results.

