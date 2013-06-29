from kombu import Exchange, Queue

# AMQP as Broker.
BROKER_URL = 'amqp://'
BROKER_CONNECTION_TIMEOUT = 4  # Default Value
BROKER_CONNECTION_RETRY = True
BROKER_CONNECTION_MAX_RETRIES = 100	# Default Value

# AMQP as database to store task state and results.
CELERY_RESULT_BACKEND = 'amqp://'

### AMQP Result Backend Settings
CELERY_RESULT_EXCHANGE = 'thugresults'
CELERY_RESULT_EXCHANGE_TYPE = 'direct'
# Msg will not be lost if broker restarts/shutdown
CELERY_RESULT_PERSISTENT = True
# Time after which task results would delete
CELERY_TASK_RESULT_EXPIRES = None		#Never Expires(eg. 24*3600->1
day)

## Queue Configuration
# Changing Default Settings
CELERY_DEFAULT_QUEUE = 'tasks'
CELERY_DEFAULT_EXCHANGE = 'tasks'
CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'
CELERY_DEFAULT_BINDING = 'tasks'
CELERY_DEFAULT_ROUTING_KEY = 'tasks'
CELERY_DEFAULT_DELIVERY_MODE = 'persistent'
# Command to Make New Queues(CELERY_QUEUES is list of Queues Instances)
'''
CELERY_QUEUES = {Queue('tasks', Exchange('tasks', durable=True),
				 routing_key='tasks', durable=True),
				 }
'''
# Routing tasks to particular Queue
CELERY_ROUTES = {'Celery_branch.tasks.Thug':
							{'queue' : 'tasks',
							'exchange': 'tasks',
							'routing_key': 'tasks'
							},
				 }

# Late acks means that tasks msgs will be acknowledged after task has been
# executed.
CELERY_ACKS_LATE = True

# Giving each worker only one task at a time
CELERYD_PREFETCH_MULTIPLIER = 1

## Concurrency Settings
# No. of Concurrent worker processes/threads executing tasks
CELERYD_CONCURRENCY = 2

## Message Settings
CELERY_MESSAGE_COMPRESSION = None

## Tasks Settings:
# Task reports its status as "started" when task is executed on worker
CELERY_TRACK_STARTED = True
CELERY_TASK_PUBLISH_RETRY = True',