# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Worldpop2Item(scrapy.Item):
    #Items in the columns of the table
    country = scrapy.Field()
    population = scrapy.Field()
    yearly_change= scrapy.Field()
    net_change= scrapy.Field()
    density= scrapy.Field()
    land_area = scrapy.Field()
    migrants_net = scrapy.Field()