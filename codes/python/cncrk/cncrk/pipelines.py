# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

import csv
import sys

class CncrkPipeline(object):
    def process_item(self, domain, item):
        return item

class CsvWriterPipeline(object):
    def __init__(self):
        self.csvwriter = csv.writer(open('cncrk_softs.csv', mode='wb')) #, encoding='utf-8'))

    def process_item(self, domain, item):
#        self.csvwriter.writerow([item['url'], item['name'][0].encode('gb2312'), item['size']])
        self.csvwriter.writerow([item['url'], item['name'][0].encode('utf-8'), item['editor'], item['size']])
        return item
