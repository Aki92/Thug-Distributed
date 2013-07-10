from __future__ import absolute_import
from ThugD.main_server import thugd
import time

# Making Thug Function to be called as task
@thugd.task
def thug(n):
	time.sleep(n)
	return "%d Job done" % n
	