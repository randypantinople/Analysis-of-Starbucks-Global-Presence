from scrapy import Spider, Request
from urban.items import UrbanItem

class UrbanSpider(Spider):
    name ='urban_spider'
    allowed_urls =["https://en.wikipedia.org"]
    start_urls=["https://en.wikipedia.org/wiki/List_of_largest_cities"]

    def parse(self, response):

        rows = response.xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr')

        for row in rows[2:]:
            city = row.xpath('./td[1]/a/text()').extract_first()
            country = row.xpath('./td[2]//a/text()').extract_first()
            city_pop = row.xpath('./td[6]/span/text()').extract_first()
            area_km2 = row.xpath('./td[7]/span/text()').extract_first()


            # Initialize a new WorldpopItem instance for each country.
            item = UrbanItem()
            item['city'] = city
            item['country']= country
            item['city_pop']= city_pop
            item['area_km2']= area_km2
            yield item


