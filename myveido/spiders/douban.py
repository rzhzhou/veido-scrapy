import scrapy
import datetime
import json
from myveido.models import (db_dyy, Category, VideoType, Star, Director,
                             VideoDetails, VideoContent)
from scrapy_splash import SplashRequest
from myveido.items import VeidoDetailsItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = [
    'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start='
        + str(x) for x in range(20, 40, 20)]


    def parse(self, response):
        rs = json.loads(response.text)
        datas = rs.get("subjects")
        for data in datas:
            item = VeidoDetailsItem()
            item['title'] = data.get('title')
            item['score'] = data.get('rate')
            item['url'] = data.get('url')
            item['thumb'] = data.get('cover')
            # items.append(item)
            yield scrapy.Request(item['url'], callback=self.parse_item)

        # print(items[1]['url'])
        # yield scrapy.Request(items[1]['url'], callback=self.parse_item)

    def parse_item(self, response):
        item = VeidoDetailsItem()
        item['url'] = response.url
        item['title'] = response.xpath('//div[@id="mainpic"]/a/img/@alt').extract()
        item['score'] = response.xpath('//div[@class="rating_self clearfix"]/strong/text()').extract()
        item['director'] = response.xpath('//div[@class="subject clearfix"]/div[@id="info"]/span[1]/span[2]/a/text()').extract()
        item['star'] = response.xpath('//div[@class="subject clearfix"]/div[@id="info"]/span[3]/span[2]//a/text()').extract()
        item['videotype'] = response.xpath('//div[@class="subject clearfix"]/div[@id="info"]//span[@property="v:genre"]/text()').extract()
        item['introduction'] = response.xpath('//div[@id="link-report"]/span/text()').extract()
        item['thumb'] = response.xpath('//div[@id="mainpic"]/a/img/@src').extract()
        # print(d_director, d_star, d_videotype, d_introduction[0].strip())
        yield item
