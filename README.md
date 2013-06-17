#**Thug Distributed Task Queuing**
================

It is the Distributed Version of Thug, which feed tasks into a Queue to be distributed among thug instances.
Thug Instances then connect to the Queue and queue automatically distributes tasks among thug instances giving
only one task at a time so that Thug Instances doesn't get loaded up with requests. Then Thug Instances process 
that tasks and give back the results to the Main Server.

##Main Server

It feeds up tasks into queue and also connects a Callback Queue with every connected thug instance to get back
the results from them.

File: `main_server.py`   
Usage: **`python main_server.py [-h] [tasks [tasks ...]]`**    

Different ways of using `main_server.py`:   
1) Task takes default Value 1:     
**`$python main_server.py`**      

2) 5 tasks for distribution feed up in Queue for Distribution:   
**`$python main_server.py 7 4 5 6 1`**   


##Thug Instance

It firstly connects to Queue and then consumes messages from it and after processing it returns the results to 
Main Server.

File: `thug_instance.py`   
Usage: **`python thug_instance.py`**   
