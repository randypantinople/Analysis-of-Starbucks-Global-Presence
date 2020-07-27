
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class WorldpopItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    country = scrapy.Field()
    population = scrapy.Field()
    yearly_change= scrapy.Field()
    net_change= scrapy.Field()
    density= scrapy.Field()
    land_area = scrapy.Field()
    migrants_net = scrapy.Field()
    
