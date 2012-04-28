# Scrapy settings for cncrk project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
# Or you can copy and paste them from where they're defined in Scrapy:
# 
#     scrapy/conf/default_settings.py
#

import cncrk

BOT_NAME = 'cncrk'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['cncrk.spiders']
NEWSPIDER_MODULE = 'cncrk.spiders'
DEFAULT_ITEM_CLASS = 'cncrk.items.CncrkItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = [
    'cncrk.pipelines.CsvWriterPipeline',
]

#EXPORT_FORMAT = 'csv_headers'
#EXPORT_FILE = 'scraped_items_with_headers.csv'
#EXPORT_FILEDS = ['name', 'price', 'description']

### todo
# export setting doesnot work
# encoding for Chinese characters
