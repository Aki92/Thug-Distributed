#!/usr/bin/env python
#
# thug.py
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA  02111-1307  USA

import logging
import json
import sys
import os

from ThugAPI import *
from Plugins.ThugPlugins import *

log = logging.getLogger("Thug")
log.setLevel(logging.WARN)

configuration_path = "/etc/thug"

class Thug(ThugAPI):
    def __init__(self, url):
        # args(url) not used in ThugAPI code so just passed URL
        ThugAPI.__init__(self, url, configuration_path)

    def analyze(self, opts):
        p = getattr(self, 'run_remote', None)

        # Dictionary format of JSON opts
        options = json.loads(opts)

        if options['version']:
            return self.thug_version

        self.set_useragent(options['useragent'])

        if options['events']:
            self.set_events(options['events'])
        if options['delay']:
            self.set_delay(options['delay'])
        if options['referer']:
            self.set_referer(options['referer'])
        if options['proxy']:
            self.set_proxy(options['proxy'])
        if options['local']:
            p = getattr(self, 'run_local')
        if options['local_nofetch']:
            p = getattr(self, 'run_local')
            self.set_no_fetch()
        if options['verbose']:
            self.set_verbose()
        if options['debug']:
            self.set_debug()
        if options['no_cache']:
            self.set_no_cache()
        if options['ast_debug']:
            self.set_ast_debug()
        if options['adobepdf']:
            self.set_acropdf_pdf(options['adobepdf'])
        if options['no_adobepdf']:
            self.disable_acropdf()
        if options['shockwave']:
            self.set_shockwave_flash(options['shockwave'])
        if options['no_shockwave']:
            self.disable_shockwave_flash()
        if options['javaplugin']:
            self.set_javaplugin(options['javaplugin'])
        if options['no_javaplugin']:
            self.disable_javaplugin()
        if options['threshold']:
            self.set_threshold(options['threshold'])
        if options['extensive']:
            self.set_extensive()
        if options['timeout']:
            self.set_timeout(options['timeout'])
        if options['urlclassifier']:
            for classifier in options['urlclassifier'].split(','):
                self.add_urlclassifier(os.path.abspath(classifier))
        if options['jsclassifier']:
            for classifier in options['jsclassifier'].split(','):
                self.add_jsclassifier(os.path.abspath(classifier))
        if options['json_logging']:
            self.set_json_logging()
        if options['file_logging']:
            self.set_file_logging()
        if options['vtquery']:
            self.set_vt_query()

        self.log_init(self.args)

        if options['logdir']:
            self.set_log_dir(options['logdir'])
        if options['output']:
            self.set_log_output(options['output'])
        if options['quiet']:
            self.set_log_quiet()

        if p:
            ThugPlugins(PRE_ANALYSIS_PLUGINS, self)()
            p(self.args)
            ThugPlugins(POST_ANALYSIS_PLUGINS, self)()

        self.log_event()
        return log
