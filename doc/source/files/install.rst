.. _install:

**************************
Libraries Used and Install
**************************


Libraries Used
##############

* **Celery** : Asynchronous Task Queue based on Distributed message passing, which is perfect choice for our implementation.

* **RabbitMQ** : Its the Message Broker. Handles queues in Celery with capability to handle millions of tasks efficiently.

* **Flower** : Monitoring & Management tool of Celery which helps us to monitor & manage all our Thug Clients working across the globe.

* **DnsPython** : Used for DNS Querying the Team Cymru Service of IP to ASN Mapping.

* **LibRabbitMQ** : This module is installed to use optimized client written in C.


Installation
############

1. RabbitMQ Server

.. code-block:: sh

		$ sudo apt-get install rabbitmq-server
		
2. Celery

.. code-block:: sh

		$ pip install celery
		
3. Flower

.. code-block:: sh

		$ pip install flower
		
4. DnsPython

.. code-block:: sh

		$ pip install dnspython

5. LibRabbitMQ: Optimizing Worker

.. code-block:: sh

		$ pip install librabbitmq

