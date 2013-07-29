.. _install:

**************************
Libraries Used and Install
**************************


Libraries Used
##############

* **Celery** : Its a Distributed Task Queuing which works perfect for our implementation.

* **RabbitMQ** : Its a Message Broker which handles the large number of clients efficiently.

* **Flower** : Its a Monitoring & Management tool of Celery which helps us to monitor & manage all our Thug Clients working across the globe.

* **DnsPython** : It is used for DNS Querying the Team Cymru Service of IP to ASN Mapping.



Installation
############

1. RabbitMQ Server

.. code-block:: sh

		$ sudo apt-get install rabbitmq-server
		
2. Celery

.. code-block:: sh

		$ sudo pip install celery
		
3. Flower

.. code-block:: sh

		$ sudo pip install flower
		
4. DnsPython

.. code-block:: sh

		$ sudo pip install dnspython

