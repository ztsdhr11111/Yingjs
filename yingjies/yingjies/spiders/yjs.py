# -*- coding: utf-8 -*-
import scrapy
from ..items import YingItem


class YjsSpider(scrapy.Spider):
    name = 'yjs'
    # allowed_domains = ['yingjiesheng.com']
    base_url = 'http://s.yingjiesheng.com/search.php?word=python&area=1056&start='
    offset = 0
    start_urls = [base_url+str(offset)]

    def parse(self, response):
        links = response.xpath('//div[@class="column1"]/ul[@class="searchResult"]/li/div/h3/a/@href').extract()
        for link in links:
            yield scrapy.Request(link, callback=self.parse_detail)

        if self.offset <= 680:
            self.offset += 10
            yield scrapy.Request(self.base_url+str(self.offset), callback=self.parse)

    def parse_detail(self, response):
        item = YingItem()
        item['pub_date'] = response.xpath('//div[@class="info clearfix"]/ol/li[1]/u/text()').extract_first()
        item['workplace'] = response.xpath('//div[@class="info clearfix"]/ol/li[2]/u/text()').extract_first()
        item['position'] = response.xpath('//div[@class="info clearfix"]/ol/li[5]/u/text()').extract_first()
        item['position_type'] = response.xpath('//div[@class="info clearfix"]/ol/li[3]/u/text()').extract_first()
        # item['job'] = response.xpath('//*[@id="wordDiv"]/div/div/text()').extract()
        item['job'] = response.xpath('//*[@id="wordDiv"]//text()').extract()
        yield item
