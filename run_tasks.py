from ThugD.thug_instances import thug
from celery import group, subtask
from json import dumps
from copy import copy
import args

class Tasks(object):
    """ Distributing Tasks on basis of arguments passed """

    def __init__(self, opts):
        """ Initializing all required queues, urls and agents """
        agt = opts.pop('include_agent')
        quf = opts.pop('queue_file')
        qu = opts.pop('queue')
        uf = opts.pop('url_file')
        ul = opts.pop('url')
        self.queue = []
        self.agent = []
        self.task = []
        self.url = []
        self.opts = opts

        if uf is None:
            self.url.extend(ul)
        else:
            self.url.extend(uf)

        if quf is None:
            if type(qu) is str:
                self.queue.append(qu)
            else:
                self.queue.extend(qu)
        else:
            self.queue.extend(quf)
        if agt is None:
            # Putting default agent
            self.agent.append('winxpie60')
        else:
            self.agent.extend(agt)

    def allocate_tasks(self):
        """ Allocating tasks to queues according to passed arguments """
        for ul in self.url:
            for qu in self.queue:
                for ag in self.agent:
                    opts = copy(self.opts)
                    opts['useragent'] = ag
                    self.task.append(thug.apply_async(args=(ul,dumps(opts),),
                                                      queue=qu))
    def get_results(self):
        """ Getting results of all allocate tasks """
        for t in self.task:
            print t.get()

if __name__ == '__main__':
    # Parsing command line arguments
    opts = vars(args.parsing())
    ta = Tasks(opts)
    ta.allocate_tasks()
    ta.get_results()