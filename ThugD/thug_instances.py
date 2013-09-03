from __future__ import absolute_import
from ThugD.main_server import thugd
import time
import sys
import os

# Adding path to sys path variable
# os.getcwd => path of parent directory where call_thug resides
sys.path.append(os.getcwd())
import call_thug

# Making Thug Function to be called as task
@thugd.task
def thug(url, opts):
    res = call_thug.Thug(url)
    log = res.analyze(opts)
    return "Done"