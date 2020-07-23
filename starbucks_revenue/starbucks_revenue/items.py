# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StarbucksRevenueItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    fiscal_year= scrapy.Field()
    region=scrapy.Field()
    ownership_type=scrapy.Field()
    num_stores=scrapy.Field()
    

