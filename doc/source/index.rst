.. Thug Distributed documentation master file, created by
   sphinx-quickstart on Sun Jul 28 17:01:26 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Thug Distributed documentation!
============================================

`ThugD <https://github.com/Aki92/Thug-Distributed>`_ stands for **Thug Distributed Task Queuing Project**. It is developed under `The Honeynet Project <https://www.honeynet.org/>`_ organization as a `GSoC <http://www.google-melange.com/>`_ Project. It is a Distributed Version of the existing `Thug Project <http://buffer.github.io/thug/>`_. 

`ThugD <https://github.com/Aki92/Thug-Distributed>`_ is developed using **Celery** [#f1]_ for Distributing tasks(URLs) among the workers. While RabbitMQ [#f2]_ and Redis [#f3]_ works as the brokers in it. It also uses Team Cymru Community Services [#f4]_ and PyDNS [#f5]_ to query its services.

Please refer to `Project Slot Page <https://www.honeynet.org/gsoc/slot3>`_ for more details.     
Stay tuned to `Project Weekly Blog <http://gsoc2013.honeynet.org/category/project-3-thug-distributed-task-queuing>`_.



.. toctree::
   :maxdepth: 2
   
   files/intro
   files/install
   files/usage
   files/download
   files/code


Indices and tables
==================

* :ref:`search`


.. rubric:: Footnotes

.. [#f1] `Celery: Distributed Task Queue <http://www.celeryproject.org/>`_

.. [#f2] `RabbitMQ <http://www.rabbitmq.com/>`_ is used as the Message Broker in Celery.

.. [#f3] `Redis <http://redis.io/>`_ is used as the Backend Broker in Celery. It is preferred then default AMQP backend broker as it don't create individual queues while returning results to server.

.. [#f4] `Team Cymru Community Service <http://www.team-cymru.org/Services/ip-to-asn.html>`_ is used for fetching country codes from IP address of the users.

.. [#f5] `PyDNS <http://pydns.sourceforge.net/>`_ is used for DNS queries over Team Cymru's IP-to-ASN service.
