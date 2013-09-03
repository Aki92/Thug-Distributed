.. _usage:

*****
Usage
*****


**1.** Run Flower

.. code-block:: sh

		$ flower
		
Open `<http://localhost:5555/>`_ in browser to access the tool.    


**2.** Using terminal go where you pasted files downloaded from Github or inside **src** folder on **thugd-master/** if downloaded from below given link. Then follow commands:

* Running Worker:

Single Worker

.. code-block:: sh

		$ celery worker -A ThugD.main_server.thugd -l info -n w1

Multiple Workers

.. code-block:: sh

		$ celery multi start w1 w2 w3 -A ThugD.main_server.thugd -l info

		
* Distributing tasks

.. code-block:: sh

		$ python run_tasks.py
		
**3.** Checking Active Queues:

.. code-block:: sh

		$ sudo rabbitmqctl list_queues

