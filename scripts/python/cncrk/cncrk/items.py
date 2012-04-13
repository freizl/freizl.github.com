# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class CncrkItem(Item):
    # define the fields for your item here like:
    url = Field()
    name = Field()
    size = Field()
    level = Field()
    editor = Field()
    desc = Field()
    download_links = Field()
