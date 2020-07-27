from scrapy import Spider, Request
from worldpop.items import WorldpopItem


class WorldpopSpider(Spider):
    name ='worldpop_spider'
    allowed_urls =["https://www.worldometers.info"]
    start_urls=["https://www.worldometers.info/world-population/population-by-country/"]

    def parse(self, response):
        # Find all the table rows
         rows = response.xpath('//*[@id="example2"]/tbody/tr') 

         for row in rows:
            country = row.xpath('./td[2]//text()').extract_first()
            population=row.xpath('./td[3]//text()').extract_first()
            yearly_change = row.xpath('./td[4]//text()').extract_first()
            net_change = row.xpath('./td[5]//text()').extract_first()
            density = row.xpath('./td[6]//text()').extract_first()
            land_area = row.xpath('./td[7]//text()').extract_first()
            migrants_net = row.xpath('./td[8]//text()').extract_first()


        # Initialize a new WorldpopItem instance for each country.
            item = WorldpopItem()
            item['country'] = country
            item['population'] = population
            item['yearly_change'] = yearly_change
            item['net_change'] = net_change
            item['density'] = density
            item['land_area'] = land_area
            item['migrants_net'] = migrants_net
            yield item

        
    



