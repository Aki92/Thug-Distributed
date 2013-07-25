#**Thug Distributed Task Queuing**

It is the Distributed Version of Thug, which feed tasks into a Queue to be distributed among thug instances.
Thug Instances then connect to the Queue and queue automatically distributes tasks among thug instances giving
only one task at a time so that Thug Instances doesn't get loaded up with requests. Then Thug Instances process 
that tasks and give back the results to the Main Server.

##Thug Worker    
It is the Thug Worker which waits for Celery to distribute tasks to it, from 2 different types of queues:    
* Generic Queue(named: "generic").   
* Geolocation Based Queue(named: according to user country code).     
Then it processes the assigned task and returns back the result which stores in "amqp" database and get displayed at task running end.

Folder: **ThugD**    
Files:    
1. `geolocation.py` : It is finding the user country code using its IP address and Team Cymru service.     
2. `celeryconfig.py` : It is the Configuration file of Celery which changes all major settings.        
3. `main_server.py` : It is main file in which Celery instance is declared and dynamically a new queue is made according to user country code.     
4. `thug_instances.py` : It contains the function to be run by thug instances working all over the world.     
      

File: `run_tasks.py`
It is used to run tasks on remote workers.      


Tools/Libraries to install:      
1. `sudo apt-get install rabbitmq-server` : Works as Message Broker .      
2. `sudo pip install -U celery` : Helps in distributing tasks among running workers.     
3. `sudo pip install flower` : Helps in monitoring and managing remote workers.     
4. `sudo pip install netifaces` : Helps in finding IP address of user.    


Usage:    
1. `celery flower` : Runs the flower sever.     
   Open **http://localhost:5555/** in browser to access the tool.    
2. `celery worker -A ThugD.main_server.thugd -l info -n w1` : Running Celery worker in foreground with **w1** as hostname. Multiple workers can be run using different hostnames.      
3. `python run_tasks.py` : Running 3 types of tasks(specified in file) on worker.       
4. `sudo rabbitmqctl list_queues` : List active queues. **(Optional)**        
