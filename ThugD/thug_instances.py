from __future__ import absolute_import
from ThugD.main_server import thugd
import call_thug
import time
import os

# Making Thug Function to be called as task
@thugd.task
def thug(url, **options):
    if not os.getenv('THUG_PROFILE', None):
        res = call_thug.Thug(url)
        log = res.analyze(**options)
    else:
        import cProfile
        import pstats
        cProfile.run('Thug(sys.argv[1:])()', 'countprof')
        p = pstats.Stats('countprof')
        res = p.print_stats()

    return log