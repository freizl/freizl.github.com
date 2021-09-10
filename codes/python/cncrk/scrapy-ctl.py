#!/usr/bin/env python

import os
os.environ.setdefault('SCRAPY_SETTINGS_MODULE', 'cncrk.settings')

from scrapy.command.cmdline import execute
execute()
