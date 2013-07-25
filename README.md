#**Thug Distributed Task Queuing**

It is the Distributed Version of Thug, in which every worker finds performance 
value of its systems and then update it into **REDIS** server's **Sorted Set**, 
by which performance values of all clients remain in sorted order at Redis
database. Then the server reads the Redis Server and distributes URLs according
to the performace value of clients.

##Thug Worker    
It is the Thug Worker which updates performance value at Redis Server and then
waits for Celery to distribute tasks to it. Then it processes the assigned task 
and returns back the result using "Redis" backend.     

Folder: **ThugD**    
Files:    
1. `geolocation.py` : It is finding the user country code using its IP address 
and Team Cymru service.     
2. `celeryconfig.py` : It is the Configuration file of Celery which changes all 
major settings.        
3. `main_server.py` : It is main file in which Celery instance is declared and 
dynamically a new queue is made according to user country code.     
4. `thug_instances.py` : It contains the function to be run by thug instances 
working all over the world.     
5. `find_send_performance.py` : It finds the performance value and then update 
that value at Redis Server.     
      

File: `distribute.py`
It is used to read Redis Database and then distribute tasks to remote workers.      


Tools/Libraries to install:      
1. `sudo apt-get install rabbitmq-server` : Works as Message Broker .      
2. `sudo pip install -U celery` : Helps in distributing tasks among running 
workers.     
3. `sudo pip install flower` : Helps in monitoring and managing remote workers.     
4. `sudo pip install dnspython` : Helps in dns querying to Team Cymru service.    
5. `sudo pip install redis` : Helps in storing performance value of all clients.

Usage:    
1. `celery flower` : Runs the flower sever.     
   Open **http://localhost:5555/** in browser to access the tool.    
2. `celery worker -A ThugD.main_server.thugd -l info -n w1` : Running Celery 
worker in foreground with **w1** as hostname. Multiple workers can be run using 
different hostnames.      
3. `python distribute.py` : Running 3 types of tasks(specified in file) on worker.       
4. `sudo rabbitmqctl list_queues` : List active queues. **(Optional)**        
